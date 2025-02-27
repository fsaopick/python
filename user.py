import json
import os
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, login, password):
        self._login = login
        self._password = password

    def proverka(self, login, password):
        pass

    def login(self):
        return self._login

    def password(self):
        return self._password

    def zagruzit(filename="/Users/andrey/Desktop/users.json"):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def sohranit(users, filename="/Users/andrey/Desktop/users.json"):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(users, file, ensure_ascii=False, indent=4)

    def registracia(login, password, role, filename="/Users/andrey/Desktop/users.json"):
        users = User.zagruzit(filename)
        if any(user["login"] == login for user in users):
            print(f"Пользователь с логином {login} уже существует")
            return False
        users.append({
            "login": login,
            "password": password,
            "role": role
        })
        User.sohranit(users, filename)
        print(f"Пользователь {login} успешно зарегистрирован как {role}")
        return True

class Igrok(User):
    def proverka(self, login, password):
        return self._login == login and self._password == password

class Admin(User):
    def __init__(self, login, password, kod):
        super().__init__(login, password)
        self._kod = kod

    def proverka(self, login, password):
        return self._login == login and self._password == password

    def proverka_admin(self, login, password, kod):
        return self.proverka(login, password) and self._kod == kod