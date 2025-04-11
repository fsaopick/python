import numpy as np
import multiprocessing as mp
import psutil
import logging
from datetime import datetime
import os
import json
import time
import signal
import threading
import queue
from typing import List, Dict, Optional, Union

class LogSaver(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.queue = queue.Queue()
        self.stop_event = threading.Event()
        self.logger = logging.getLogger('MatrixMultiplier')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        if not self.logger.handlers:
            file_handler = logging.FileHandler('matrix.log', mode='w', encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
        
        self.start()

    def run(self):
        while not self.stop_event.is_set():
            try:
                level, message = self.queue.get(timeout=0.1)
                if hasattr(self.logger, level.lower()):
                    getattr(self.logger, level.lower())(message)
            except queue.Empty:
                continue

    def log(self, level: str, message: str):
        self.queue.put((level, message))

    def stop(self):
        self.stop_event.set()
        self.join()

class ResultSaver(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.queue = queue.Queue()
        self.stop_event = threading.Event()
        self.log_saver = LogSaver()
        self.start()

    def run(self):
        while not self.stop_event.is_set():
            try:
                data, filename = self.queue.get(timeout=0.1)
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    self.log_saver.log('INFO', f"результаты сохранены в {filename}")
                except Exception as e:
                    self.log_saver.log('ERROR', f"ошибка сохранения: {str(e)}")
            except queue.Empty:
                continue

    def save(self, data: Dict, filename: str):
        self.queue.put((data, filename))

    def stop(self):
        self.stop_event.set()
        self.join()

class MatrixMultiplier:
    def __init__(self):
        self.cpu_info = self._get_cpu_info()
        self.log_saver = LogSaver()
        self.result_saver = ResultSaver()
        self.log_saver.log('INFO', f"доступно ядер: {self.cpu_info['cores']}")

    def _get_cpu_info(self) -> Dict:
        cpu_load = psutil.cpu_percent(interval=1)
        available_cores = max(1, mp.cpu_count() - int(mp.cpu_count() * (cpu_load / 100)))
        
        return {
            'cores': mp.cpu_count(),
            'load': cpu_load,
            'available': available_cores
        }

    def check_sizes(self, mat1: List[List[int]], mat2: List[List[int]]) -> bool:
        if len(mat1[0]) != len(mat2):
            self.log_saver.log('ERROR', f"неверные размеры: {len(mat1)}x{len(mat1[0])} и {len(mat2)}x{len(mat2[0])}")
            return False
        return True

    def create_random_matrix(self, rows: int, cols: int) -> List[List[int]]:
        matrix = (np.random.randint(1, 11, size=(rows, cols))).tolist()
        self.log_saver.log('DEBUG', f"создана матрица {rows}x{cols} со значениями 1-10")
        return matrix

    def _worker(self, task_queue: mp.Queue, result_queue: mp.Queue):
        log_saver = LogSaver()
        
        while True:
            task = task_queue.get()
            if task is None:
                break
                
            mat1, mat2, row_indices = task
            try:
                res = []
                for i in row_indices:
                    row = []
                    for j in range(len(mat2[0])):
                        row.append(sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0]))))
                    res.append((i, row))
                    
                result_queue.put(res)
                log_saver.log('DEBUG', f"обработаны строки: {row_indices}")
                
            except Exception as e:
                log_saver.log('ERROR', f"ошибка в процессе: {str(e)}")
                result_queue.put(None)

    def multiply(self, mat1: List[List[int]], 
               mat2: List[List[int]],
               num_proc: Optional[int] = None) -> Optional[List[List[int]]]:
        if not self.check_sizes(mat1, mat2):
            return None

        if num_proc is None:
            num_proc = self.cpu_info['available']
        else:
            num_proc = min(num_proc, self.cpu_info['available'])

        rows = len(mat1)
        task_queue = mp.Queue()
        result_queue = mp.Queue()

        processes = []
        for _ in range(num_proc):
            p = mp.Process(target=self._worker, args=(task_queue, result_queue))
            p.start()
            processes.append(p)

        chunk_size = max(1, rows // num_proc)
        for i in range(0, rows, chunk_size):
            task_queue.put((
                mat1,
                mat2,
                list(range(i, min(i + chunk_size, rows)))
            ))

        for _ in range(num_proc):
            task_queue.put(None)

        result = [[0 for _ in range(len(mat2[0]))] for _ in range(rows)]
        received = 0
        while received < rows:
            res = result_queue.get()
            if res is None:
                continue
                
            for i, row in res:
                result[i] = row
                received += 1

        for p in processes:
            p.join()

        self.log_saver.log('INFO', "умножение завершено")
        return result

    def save_results(self, data: Dict, filename: str):
        self.result_saver.save(data, filename)

def main():
    log_saver = LogSaver()
    
    try:
        multiplier = MatrixMultiplier()
        
        m = int(input("введите число строк первой матрицы: "))
        n = int(input("введите число столбцов первой матрицы/строк второй: "))
        k = int(input("введите число столбцов второй матрицы: "))
        
        cpu_info = multiplier._get_cpu_info()
        max_proc = cpu_info['available']
        print(f"доступно процессов (загрузка CPU {cpu_info['load']}%): {max_proc}")
        
        proc = int(input(f"введите число процессов (1-{max_proc}): "))
        proc = max(1, min(proc, max_proc))

        mat1 = multiplier.create_random_matrix(m, n)
        mat2 = multiplier.create_random_matrix(n, k)
        
        print("\nматрица A:")
        print(np.array(mat1))
        print("\nматрица B:")
        print(np.array(mat2))

        start_time = time.time()
        res = multiplier.multiply(mat1, mat2, proc)
        elapsed = time.time() - start_time

        if res is not None:
            print("\nрезультат:")
            print(np.array(res))
            
            result_data = {
                'parameters': {
                    'rows_mat1': m,
                    'cols_mat1': n,
                    'cols_mat2': k,
                    'processes': proc,
                    'time_sec': round(elapsed, 2)
                },
                'matrix_a': mat1,
                'matrix_b': mat2,
                'result': res,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            multiplier.save_results(result_data, "results.json")
            
            log_saver.log('INFO', f"время выполнения: {elapsed:.2f} сек")

    except ValueError:
        log_saver.log('ERROR', "ошибка ввода числа")
    except Exception as e:
        log_saver.log('ERROR', f"неожиданная ошибка: {str(e)}")
    finally:
        log_saver.log('INFO', "завершение работы программы")
        time.sleep(0.5)

if __name__ == "__main__":
    mp.freeze_support()
    signal.signal(signal.SIGINT, lambda *_: exit())
    main()