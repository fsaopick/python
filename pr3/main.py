from user import Igrok, Admin, User
from computer_club import ComputerClub
from review_system import ReviewSystem
from order_system import OrderSystem


def main():
    print('Добро пожаловать в компьютерный клуб "Кузнечик"')

    computer_club = ComputerClub()
    review_system = ReviewSystem()
    order_system = OrderSystem(computer_club)

    while True:
        print("\nГлавное меню:")
        print("1. Зарегистрироваться")
        print("2. Войти")
        print("3. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            registracia()

        elif choice == "2":
            user = avtorizacia()
            if user:
                if user["role"] == "igrok":

                    igrok = Igrok(user["login"], user["password"])
                    menu_igroka(computer_club, order_system, review_system)
                    
                elif user["role"] == "admin":

                    admin = Admin(user["login"], user["password"], 52)
                    menu_admina(computer_club)

        elif choice == "3":
            print("Выход из программы")
            break

        else:
            print("Вы выбрали не то, попробуйте снова")

def vybor():
    while True:
        try:
            choice = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
            if choice < 1 or choice > 2:
                print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
            else:
                print(f"Ваш выбор: {choice}")
                return choice
        except ValueError:
            print("Вы должны ввести число")

def menu_igroka(computer_club, order_system, review_system):
    while True:
        print("\n Меню игрока:")
        print("1. Просмотреть залы")
        print("2. Просмотреть продукты")
        print("3. Сделать заказ")
        print("4. Оставить отзыв")
        print("5. Просмотреть все отзывы")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nСписок залов:")

            for idx, zal in enumerate(computer_club.zaly):
                print(f"{idx + 1}. {zal['nazvanie']} - {zal['cena']} руб./час")

            sort_choice = input("Хотите отсортировать залы? (1 - Да, 2 - Нет): ")

            if sort_choice == "1":

                klyuch = input("Введите ключ для сортировки (nazvanie, cena, reiting, chasy): ")
                obratno = input("Сортировать по убыванию? (1 - Да, 2 - Нет): ") == "1"
                computer_club.sortirovat_zaly(klyuch, obratno)

        elif choice == "2":
            print("\nСписок продуктов:")

            for idx, produkt in enumerate(computer_club.produkty):
                print(f"{idx + 1}. {produkt['nazvanie']} - {produkt['cena']} руб.")

            produkt_choice = input("Хотите добавить продукт в корзину? (1 - Да, 2 - Нет): ")

            if produkt_choice == "1":
                nazvanie = input("Введите название продукта: ")
                order_system.dobavit_v_korzinu(nazvanie)

        elif choice == "3":
            print("\nСоздание заказа:")

            nomer_zala = int(input("Введите номер зала: ")) - 1
            chasy = int(input("Введите количество часов: "))

            order_system.sozdat_zakaz(nomer_zala, chasy)
            order_system.pokazat_korzinu()

        elif choice == "4":
            print("\nОставьте отзыв:")

            text = input("Введите текст отзыва: ")
            ocenka = int(input("Введите оценку (от 1 до 5): "))

            review_system.dobavit_otzyv(text, ocenka)

        elif choice == "5":
            review_system.pokazat_otzyvy()

        elif choice == "6":
            print("Выход из меню игрока")
            break

        else:
            print("Вы выбрали не то, попробуйте снова")

def menu_admina(computer_club):
    while True:
        print("\nМеню администратора:")
        print("1. Добавить зал")
        print("2. Добавить продукт")
        print("3. Экспортировать данные")
        print("4. Импортировать данные")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nДобавление нового зала:")

            nazvanie = input("Введите название зала: ")
            kompyutery = int(input("Введите количество компьютеров: "))
            reiting = int(input("Введите рейтинг: "))
            cena = int(input("Введите цену за час: "))
            chasy = int(input("Введите количество часов работы: "))
            computer_club.dobavit_zal(nazvanie, kompyutery, reiting, cena, chasy)

            print("зал добавлен")

        elif choice == "2":
            print("\nДобавление нового продукта:")

            nazvanie = input("Введите название продукта: ")
            cena = int(input("Введите цену продукта: "))
            computer_club.dobavit_produkt(nazvanie, cena)

            print("Продукт добавлен")

        elif choice == "3":
            computer_club.export_data()
            print("Данные успешно экспортированы")

        elif choice == "4":
            computer_club.import_data()
            print("Данные успешно импортированы")

        elif choice == "5":
            print("Выход из меню администратора")
            break

        else:
            print("Вы выбрали не то, попробуйте снова")

def registracia():
    print("\nРегистрация:")

    while True:
        role = input("Выберите роль (igrok/admin): ").lower()
        if role in ["igrok", "admin"]:
            break
        print("Неверная роль. Допустимые значения: igrok, admin.")

    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if User.registracia(login, password, role):
        print("Регистрация завершена!")
    else:
        print("Регистрация не удалась")

def avtorizacia():
    print("\nАвторизация:")

    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    users = User.zagruzit()

    for user in users:
        if user["login"] == login and user["password"] == password:
            print(f"Добро пожаловать, {login}!")
            return user
        
    print("неверный логин или пароль")
    return None

if __name__ == "__main__":
    main()