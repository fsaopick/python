import json
import os

class ComputerClub:
    def __init__(self):
        self._zaly = []
        self._produkty = []
        
        self._filename = "/Users/andrey/Desktop/data.json"
        self.import_data()  

    def zaly(self):
        return self._zaly

    def produkty(self):
        return self._produkty

    def dobavit_zal(self, nazvanie, kompyutery, reiting, cena, chasy):
        self._zaly.append({
            'nazvanie': nazvanie,
            'kompyutery': kompyutery,
            'reiting': reiting,
            'cena': cena,
            'chasy': chasy
        })
        self.export_data()  

    def dobavit_produkt(self, nazvanie, cena):
        self._produkty.append({
            "nazvanie": nazvanie,
            "cena": cena
        })
        self.export_data()  

    def sortirovat_zaly(self, klyuch, obratno=False):
        if klyuch not in ["nazvanie", "kompyutery", "reiting", "cena", "chasy"]:
            print("Некорректный ключ для сортировки")
            return
        self._zaly.sort(key=lambda x: x[klyuch], reverse=obratno)
        print(f"Залы отсортированы по {klyuch} ({'по убыванию' if obratno else 'по возрастанию'})")

    def export_data(self):
        data = {
            "zaly": self._zaly,
            "produkty": self._produkty
        }
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные успешно экспортированы в файл {self._filename}")

    def import_data(self):
        try:
            if os.path.exists(self._filename):
                with open(self._filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self._zaly = data.get("zaly", [])
                    self._produkty = data.get("produkty", [])
                print(f"Данные успешно импортированы из файла {self._filename}")
            else:
                print(f"Файл {self._filename} не найден., создается новый")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла {self._filename}, возможно, некорректный JSON-файл.")