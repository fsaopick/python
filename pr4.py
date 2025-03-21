import json
import os
import threading
import time
from datetime import datetime

LICENSE_KEY = "123"  
LICENSE_TIME = 1800
start_time = time.time()  

license_ok = True  
license_activated = False  

class UserData:
    def __init__(self, username):
        self.username = username
        self.eda = []  
        self.data_file = f"{username}_data.json"
        self.load_license_data()

    def load_license_data(self):
        users = load_users()
        for user in users:
            if user["login"] == self.username:
                self.license_activated = user.get("license_activated", False)
                self.trial_time_used = user.get("trial_time_used", 0)
                break

    def save_license_data(self):
        users = load_users()
        for user in users:
            if user["login"] == self.username:
                user["license_activated"] = self.license_activated
                user["trial_time_used"] = self.trial_time_used
                break
        save_users(users)

    def add_eda(self, food, date_time, calories, protein, fat, carbs):
        self.eda.append({
            'food': food,
            'date_time': date_time,
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'carbs': carbs
        })

    def edit_eda(self, food, new_food, new_date_time, new_calories, new_protein, new_fat, new_carbs):
        for entry in self.eda:
            if entry['food'] == food:
                entry['food'] = new_food
                entry['date_time'] = new_date_time
                entry['calories'] = new_calories
                entry['protein'] = new_protein
                entry['fat'] = new_fat
                entry['carbs'] = new_carbs
                return
        print("запись не найдена")

    def delete_eda(self, food):
        self.eda = [entry for entry in self.eda if entry['food'] != food]

    def view_eda(self):
        if not self.eda:
            print("записей нет")
        else:
            for idx, entry in enumerate(self.eda):
                print(f"{idx + 1} {entry['food']} - {entry['date_time']} - "
                      f"{entry['calories']} ккал, б: {entry['protein']}г, "
                      f"ж: {entry['fat']}г, у: {entry['carbs']}г")

    def save_data(self):
        try:
            data = {
                "eda": self.eda
            }
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("данные сохранены")
        except Exception as e:
            print("ошибка при сохранении данных")
            LoggerThread.log_error(self.username, f"ошибка при сохранении данных: {e}")

    def load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.eda = data.get("eda", [])
                print(f"данные пользователя {self.username} загружены")
        except json.JSONDecodeError as e:
            print(f"ошибка чтения файла {self.data_file}")
            LoggerThread.log_error(self.username, f"ошибка чтения файла {self.data_file}: {e}")
        except Exception as e:
            print("ошибка при загрузке данных")
            LoggerThread.log_error(self.username, f"ошибка при загрузке данных: {e}")

class LoggerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.running = True

    def run(self):
        while self.running:
            time.sleep(1)  

    @staticmethod
    def log_action(username, action):
        log_entry = f"[info] [{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [{username}] – {action}\n"
        with open("app.log", "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)

    @staticmethod
    def log_error(username, error_message):
        log_entry = f"[error] [{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [{username}] – {error_message}\n"
        with open("app.log", "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)

    def stop(self):
        self.running = False

def import_data(user_data):
    print("импорт данных")
    time.sleep(2)  
    user_data.load_data()  

def auto_save(user_data, save_event):
    while True:
        save_event.wait()  
        user_data.save_data()
        save_event.clear()  

def check_license():
    global license_ok
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= LICENSE_TIME and not license_activated:
            license_ok = False
            print("пробная лицензия завершена, введите ключ для продолжения")
            break
        time.sleep(1)  

def enter_key(user_data):
    global license_ok, license_activated
    while True:
        key = input("введите ключ: ")
        if key == LICENSE_KEY:
            license_ok = True
            license_activated = True
            user_data.license_activated = True
            user_data.save_license_data()
            print("ключ принят, доступ восстановлен")
            break
        else:
            print("неверный ключ, попробуйте снова")

def registracia():
    print("\nрегистрация")
    login = input("введите логин: ")
    password = input("введите пароль: ")

    users = load_users()
    if any(user["login"] == login for user in users):
        print("пользователь уже существует")
        return None
    else:
        users.append({
            "login": login,
            "password": password,
            "license_activated": False,
            "trial_time_used": 0
        })
        save_users(users)
        print("регистрация успешна")
        return login

def avtorizacia():
    print("\nавторизация")
    login = input("введите логин: ")
    password = input("введите пароль: ")

    users = load_users()
    for user in users:
        if user["login"] == login and user["password"] == password:
            print("авторизация успешна")
            return login
    print("неверный логин или пароль")
    return None

def load_users():
    try:
        if os.path.exists("users.json"):
            with open("users.json", 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return []
    except json.JSONDecodeError as e:
        print("ошибка чтения файла users.json")
        LoggerThread.log_error("system", f"ошибка чтения файла users.json: {e}")
        return []
    except Exception as e:
        print("ошибка при загрузке данных пользователей")
        LoggerThread.log_error("system", f"ошибка при загрузке данных пользователей: {e}")
        return []

def save_users(users):
    try:
        with open("users.json", 'w', encoding='utf-8') as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("ошибка сохранения данных пользователей")
        LoggerThread.log_error("system", f"ошибка сохранения данных пользователей: {e}")

def main():
    global license_ok, license_activated

    license_thread = threading.Thread(target=check_license, daemon=True)
    license_thread.start()

    logger_thread = LoggerThread()
    logger_thread.start()

    print('добро пожаловать в дневник питания')
    while True:
        print("\nглавное меню")
        print("1 зарегистрироваться")
        print("2 войти")
        print("3 выйти")
        choice = input("выберите действие: ")

        if choice == "1":
            username = registracia()
            if username:
                user_data = UserData(username)
                LoggerThread.log_action(username, "пользователь зарегистрирован")
                break

        elif choice == "2":
            username = avtorizacia()
            if username:
                user_data = UserData(username)
                LoggerThread.log_action(username, "пользователь авторизован")
                break

        elif choice == "3":
            print("выход")
            LoggerThread.log_action("system", "завершение работы программы")
            logger_thread.stop()  
            return

        else:
            print("неверный выбор попробуйте снова")
            LoggerThread.log_error("system", "неверный выбор в главном меню")

    if not license_ok and not user_data.license_activated:
        enter_key(user_data)

    if not license_ok and not user_data.license_activated:
        print("доступ к программе заблокирован из-за отсутствия лицензии")
        return

    import_thread = threading.Thread(target=import_data, args=(user_data,))
    import_thread.start()
    import_thread.join()  

    save_event = threading.Event()

    save_thread = threading.Thread(target=auto_save, args=(user_data, save_event), daemon=True)
    save_thread.start()

    while True:
        if not license_ok and not user_data.license_activated:
            print("пробная лицензия завершена, введите ключ для продолжения")
            enter_key(user_data)
            if not license_ok and not user_data.license_activated:
                print("доступ к программе заблокирован из-за отсутствия лицензии")
                break

        print("\nменю")
        print("1 добавить запись питания")
        print("2 редактировать запись питания")
        print("3 удалить запись питания")
        print("4 просмотреть все записи")
        print("5 выйти")
        choice = input("выберите действие: ")

        if choice == "1":
            print("\nдобавление записи питания")
            food = input("введите название еды: ")
            date_choice = input("ввести дату и время вручную (1) или использовать текущее время (2)? ")
            if date_choice == "1":
                date_time = input("введите дату и время (формат гггг-мм-дд чч:мм): ")
            else:
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

            try:
                calories = int(input("введите калории: "))
                protein = int(input("введите белки (г): "))
                fat = int(input("введите жиры (г): "))
                carbs = int(input("введите углеводы (г): "))

                user_data.add_eda(food, date_time, calories, protein, fat, carbs)
                save_event.set()  
                LoggerThread.log_action(user_data.username, "добавлена запись питания")
                print("запись добавлена")
            except ValueError as e:
                print("ошибка: введены некорректные данные пожалуйста, введите числа")
                LoggerThread.log_error(user_data.username, f"ошибка ввода данных: {e}")

        elif choice == "2":
            print("\nредактирование записи питания")
            food = input("введите название еды для редактирования: ")
            new_food = input("введите новое название еды: ")
            new_date_time = input("введите новую дату и время (формат гггг-мм-дд чч:мм): ")
            try:
                new_calories = int(input("введите новые калории: "))
                new_protein = int(input("введите новые белки (г): "))
                new_fat = int(input("введите новые жиры (г): "))
                new_carbs = int(input("введите новые углеводы (г): "))

                user_data.edit_eda(food, new_food, new_date_time, new_calories, new_protein, new_fat, new_carbs)
                save_event.set()  
                LoggerThread.log_action(user_data.username, "запись питания отредактирована")
                print("запись обновлена")
            except ValueError as e:
                print("ошибка: введены некорректные данные пожалуйста, введите числа")
                LoggerThread.log_error(user_data.username, f"ошибка ввода данных: {e}")

        elif choice == "3":
            print("\nудаление записи питания")
            food = input("введите название еды для удаления: ")
            user_data.delete_eda(food)
            save_event.set()  
            LoggerThread.log_action(user_data.username, "запись питания удалена")
            print("запись удалена")

        elif choice == "4":
            print("\nвсе записи питания")
            user_data.view_eda()
            LoggerThread.log_action(user_data.username, "просмотр всех записей питания")

        elif choice == "5":
            print("выход")
            user_data.save_data()  
            if not user_data.license_activated:

                elapsed_time = time.time() - start_time
                user_data.trial_time_used += elapsed_time
                user_data.save_license_data()
                print(f"Вы использовали пробную версию в течение {user_data.trial_time_used:.2f} секунд.")

            LoggerThread.log_action(user_data.username, "пользователь вышел из программы")
            logger_thread.stop()
            break

        else:
            print("неверный выбор попробуйте снова")
            LoggerThread.log_error(user_data.username, "неверный выбор в меню")

if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()

    main_thread.join()

    print("ожидание завершения фонового потока")
    time.sleep(2)  
    print("программа завершена")