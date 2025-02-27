import json
import os

class ReviewSystem:
    def __init__(self):
        self._otzyvy = []
        self._filename = "/Users/andrey/Desktop/data1.json"
        self.import_data()  

    def dobavit_otzyv(self, text, ocenka):
        self._otzyvy.append({'text': text, 'ocenka': ocenka})
        self.export_data()  

    def udalit_otzyv(self, index):
        if 0 <= index < len(self._otzyvy):
            self._otzyvy.pop(index)
            self.export_data()  

    def pokazat_otzyvy(self):
        if not self._otzyvy:
            print("Нет отзывов для отображения.")
        else:
            print("\nВсе отзывы:")
            for idx, otzyv in enumerate(self._otzyvy):
                print(f"{idx + 1}. {otzyv['text']} (Оценка: {otzyv['ocenka']})")

    def export_data(self):
        data = {
            "otzyvy": self._otzyvy
        }
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные об отзывах успешно экспортированы в файл {self._filename}")

    def import_data(self):
        try:
            if os.path.exists(self._filename):
                with open(self._filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self._otzyvy = data.get("otzyvy", [])
                print(f"Данные об отзывах успешно импортированы из файла {self._filename}")
            else:
                print(f"Файл {self._filename} не найден, создан новый")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла {self._filename},возможно, некорректный JSON-файл")