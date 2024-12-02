from functools import reduce
print('Добро подаловать в компьютерный клуб "Кузнечик"')
print('Авторизация')

pr1 = 1
while pr1 == 1:
    try:
        otvet = int(input("Вы уже зарегистрированы? 1 - Да, 2 - Нет:     "))

        if otvet < 1 or otvet > 2:
            print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
        else:
            print(f"Ваш выбор: {otvet}")
            pr1 = 0  
    except ValueError:
        print("Вы должны ввести число")

playyerr  = {
    "login": "1",
    "parol": "1",
    }
admin = {
    "login": "1",
    "parol": "1",
    }

loginhranenyead = admin.get("login")
parolhranenyead = admin.get("parol")

loginhranenyepl = playyerr.get("login")
parolhranenyepl = playyerr.get("parol")

computers = [{'title': 'Зал первый', 'colvocomputers': 10, 'rating': 5, 'price': 1360, 'vchas': 15},
                        {'title': 'Зал второй', 'colvocomputers': 15, 'rating': 4, 'price': 1500, 'vchas': 20},
                        {'title': 'Зал третий', 'colvocomputers': 20, 'rating': 5, 'price': 2000, 'vchas': 10},
                        {'title': 'Зал четвертый', 'colvocomputers': 10, 'rating': 5, 'price': 1200, 'vchas': 5},
                        {'title': 'Зал пятый', 'colvocomputers': 15, 'rating': 5, 'price': 1500, 'vchas': 11},
                        {'title': 'Зал шестой', 'colvocomputers': 10, 'rating': 3, 'price': 1300, 'vchas': 12},
                        {'title': 'Зал седьмой', 'colvocomputers': 5, 'rating': 4, 'price': 1400, 'vchas': 18},
                        {'title': 'Зал восьмой', 'colvocomputers': 5, 'rating': 5, 'price': 1100, 'vchas': 7},
                        {'title': 'Зал девятый', 'colvocomputers': 10, 'rating': 4, 'price': 1050, 'vchas': 20},
                        {'title': 'Зал десятый', 'colvocomputers': 25, 'rating': 5, 'price': 3000, 'vchas': 11}]

products = [
                            {"name": "Сникерс", "price": 70},
                            {"name": "Энергетик Адреналин", "price": 120},
                            {"name": "Чипсы Лейс", "price": 200},
                            {"name": "Киткат", "price": 70},
                            {"name": "Кока-кола", "price": 150},
                            {"name": "Энергетик Берн", "price": 110},
                            {"name": "Твикс", "price": 90},
                            {"name": "Энергетик Редбулл", "price": 250},
                            {"name": "Шипучка", "price": 50},
                            {"name": "Чипсы крабовые", "price": 150},
                        ]

prodolzh = 1
while (prodolzh == 1):
    prod = 1
    while (prod == 1):
        if (otvet == 1):

            pr2 = 1
            while pr2 == 1:
                try:
                    otvet1 = int(input("За кого вы хотите зайти? 1 - Игрок, 2 - Админ:     "))

                    if otvet1 < 1 or otvet1 > 2:
                        print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                    else:
                        print(f"Ваш выбор: {otvet1}")
                        pr2 = 0  
                except ValueError:
                    print("Вы должны ввести число")

            
            if (otvet1 == 1):
                logininput = input("Введите логин: ")
                parolinput = input("Введите пароль: ")

                if (logininput == loginhranenyepl) and (parolinput == parolhranenyepl):
                    print("Вы успешно авторизированы")
                    prod = 0
                    ar = 1
                else:
                    print("Вы ввели неправильный логин или пароль")

                    pr3 = 1
                    while pr3 == 1:
                        try:
                            prod = int(input("Хотите поробовать зарегистрироваться заного? 1 - Да, 2 - Нет: "))

                            if prod < 1 or prod > 2:
                                print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                            else:
                                print(f"Ваш выбор: {prod}")
                                pr3 = 0  
                        except ValueError:
                            print("Вы должны ввести число")
                    

            elif (otvet1 == 2):

                logininput = input("Введите логин: ")
                parolinput = input("Введите пароль: ")

                if (logininput == loginhranenyead) and (parolinput == parolhranenyead):
                    print("Вы успешно авторизированы")
                    prod = 0
                    ar = 1
                else:
                    print("Вы ввели неправильный логин или пароль")
                    pr3 = 1
                    while pr3 == 1:
                        try:
                            prod = int(input("Хотите поробовать зарегистрироваться заного? 1 - Да, 2 - Нет: "))

                            if prod < 1 or prod > 2:
                                print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                            else:
                                print(f"Ваш выбор: {prod}")
                                pr3 = 0  
                        except ValueError:
                            print("Вы должны ввести число")
            else:
                print("Вы ввели неправильную цифру")
                prod = 1

        elif (otvet == 2):
            pr2 = 1
            while pr2 == 1:
                try:
                    otvet1 = int(input("За кого вы хотите зарегистрироваться? 1 - Игрок, 2 - Админ:     "))

                    if otvet1 < 1 or otvet1 > 2:
                        print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                    else:
                        print(f"Ваш выбор: {otvet1}")
                        pr2 = 0  
                except ValueError:
                    print("Вы должны ввести число")
            
            if (otvet1 == 1):
                playyerr["login"] = input("Введите логин: ")
                playyerr["parol"] = input("Введите пароль: ")

                login = playyerr.pop("login")
                parol = playyerr.pop("parol")

                prod = 0
                ar = 1

            else:
                admin["login"] = input("Введите логин: ")
                admin["parol"] = input("Введите пароль: ")

                pr10 = 1
                while pr10 == 1:
                    try:
                        a = int(input("Введите пароль доступа к администрированию: "))

                        if a == 52:
                            pr10 = 0  
                        else:
                            print("Вы ввели не ту цифру, попробуйте заново")
                            pr10 = 1
                    except ValueError:
                        print("Вы должны ввести число")

                login = admin.pop("login")
                parol = admin.pop("parol")
                prod = 0
                ar = 1
        else:
            print("Вы ввели неправильную цифру")
            pr1 = 1
        
            
    print ("--------------------------------------------------------------")
    

    if (otvet1 == 1 and ar == 1):
        print ("Меню")
        prod1 = 1
        while (prod1 == 1):
            print ("Выберите действие:")
            print ("    1. Просмотреть списки доступных залов для гейминга")
            print ("    2. Посмотреть список доступных товаров для покупки(еда и напитки)")
            print ("    3. Отзывы")
            print ("    4. Сделать заказ на аренду и рассчитать стоимость")
            print ("    5. Выйти")

            pr11 = 1
            while pr11 == 1:
                try:
                    vibor = int(input())

                    if vibor < 1 or vibor > 5:
                        print("Вы ввели не ту цифру, попробуйте снова")
                    else:
                        print(f"Ваш выбор: {vibor}")
                        pr11 = 0  
                except ValueError:
                    print("Вы должны ввести число")
            
            
            if vibor == 1:
                print ("В нашем компьютерном клубе доступно несколько залов")
                number = 1
                for computer in computers:
                    print(f"{number}. Название: {computer['title']}, Количество компьютеров: {computer['colvocomputers']}, Рейтинг: {computer['rating']}, Цена: {computer['price']}, Часы работы: {computer['vchas']}")
                    number += 1

                pr12 = 1
                while pr12 == 1:
                    try:
                        sortvibor = int(input("Хотите воспользоваться функцией сортировки по критериям? 1 - Да 2 - Нет: "))

                        if sortvibor < 1 or sortvibor > 2:
                            print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                        else:
                            print(f"Ваш выбор: {sortvibor}")
                            pr12 = 0  
                    except ValueError:
                        print("Вы должны ввести число")


                if sortvibor == 1:
                    def display_computer_halls(computers):
                        print("Выберите критерии для отображения (введите через запятую, в формате 1, 2, 3..):")
                        print("1 - Количество компьютеров в зале")
                        print("2 - Рейтинг зала")
                        print("3 - Цена за час")
                        print("4 - Максимальное количество часов")
                        

                        pr13 = 1
                        while pr13 == 1:
                            try:
                                selected_criteria = list(map(int, input().split(', ')))
                                if len(selected_criteria) > 4:
                                    raise ValueError("Необходимо ввести не больше 4 критериев.")
                                return selected_criteria
                            except ValueError:
                                print("Вы ввели некорректно, попробуйте снова")

                        for computer in computers:
                            output = [f"Зал: {computer['title']}"]
                            if 1 in selected_criteria:
                                output.append(f"количество компьютеров: {computer['colvocomputers']}")
                            if 2 in selected_criteria:
                                output.append(f"рейтинг: {computer['rating']}")
                            if 3 in selected_criteria:
                                output.append(f"цена за час: {computer['price']}")
                            if 4 in selected_criteria:
                                output.append(f"максимальное количество часов: {computer['vchas']}")
                            
                            print(" - ".join(output))
                    display_computer_halls(computers)

                    selected_criteria = list(map(int, input().split(',')))
                else:
                    print("Вы ввели что-то не то")

                pr14 = 1
                while pr14 == 1:
                    try:
                        filtr = int(input("Хотите воспользоваться функцией фильрации по всем залам? 1 - Да, 2 - Нет:  "))

                        if filtr < 1 or filtr > 2:
                            print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
                        else:
                            print(f"Ваш выбор: {filtr}")
                            pr14 = 0  
                    except ValueError:
                        print("Вы должны ввести число")


                if filtr == 1:
                    
                        print("Выберите критерии для отображения:")
                        colvo = int(input("1 - Больше 10 компьютеров в зале, 2 - Меньше 10 компьютеров в зале: "))

                        if colvo == 1:
                            cena = int(input("1 - Больше 1300 ру/ч, 2 - Меньше 1300 ру/ч: "))

                            if cena == 1:
                                chasi = int(input("1 - Больше 10 возможных часов снятия зала, 2 - Меньше 10 возможных часов снятия зала: "))

                                for computer in filter(lambda x: x["colvocomputers"] > 10 and x["price"] > 1300 and x["vchas"] > 10, computers):
                                    print(computer)  

                            elif cena == 2:
                                chasi = int(input("1 - Больше 10 возможных часов снятия зала , 2 - Меньше 10 возможных часов снятия зала: "))
                                
                                for computer in filter(lambda x: x["colvocomputers"] > 10 and x["price"] < 1300 and x["vchas"] < 10, computers):
                                    print(computer) 

                            else:
                                print("Вы ввели чтото не то")    

                        elif colvo == 2:
                            cena = int(input("1 - Больше 1300 ру/ч, 2 - Меньше 1300 ру/ч: "))

                            if cena == 1:
                                chasi = int(input("1 - Больше 10 возможных часов снятия зала, 2 - Меньше 10 возможных часов снятия зала: "))

                                if chasi == 1:

                                    for computer in filter(lambda x: x["colvocomputers"] < 10 and x["price"] > 1300 and x["vchas"] > 10, computers):
                                        print(computer)  

                                elif chasi == 2:

                                    for computer in filter(lambda x: x["colvocomputers"] < 10 and x["price"] > 1300 and x["vchas"] < 10, computers):
                                        print(computer)  

                            elif cena == 2:
                                chasi = int(input("1 - Больше 10 возможных часов снятия зала, 2 - Меньше 10 возможных часов снятия зала: "))

                                if chasi == 1:

                                    for computer in filter(lambda x: x["colvocomputers"] < 10 and x["price"] < 1300 and x["vchas"] > 10, computers):
                                        print(computer) 

                                elif chasi == 2:

                                    for computer in filter(lambda x: x["colvocomputers"] < 10 and x["price"] < 1300 and x["vchas"] < 10, computers):
                                        print(computer)  
                        else:
                            print("Вы ввели что-то не то")

                elif filtr == 2:
                    print("Вы возвращетесь в меню")
                    prod1 = 1
                else:
                    print("Вы ввели что-то не то")
            
            elif vibor == 2:
            
                number1 = 1
                for product in products:
                    print(f"{number1}. Название: {product['name']}, Цена: {product['price']} руб.")
                    number1 += 1
                cart = []

                def add_to_cart(product_name):
                    product = next((item for item in products if item["name"] == product_name), None)

                    if product:
                        cart.append(product)
                        print(f"{product_name} добавлен в корзину.")
                    else:
                        print("Продукт не найден.")

                def calculate_total(cart):
                    return reduce(lambda total, item: total + item["price"], cart, 0)
                
                prod2 = 1
                while prod2 == 1:
                    nomerproducta = int(input("Выберите номер продукта, чтобы добавить его в корзину: "))

                    if nomerproducta == 1:
                        add_to_cart("Сникерс")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 2:
                        add_to_cart("Энергетик Адреналин")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 3:
                        add_to_cart("Чипсы Лейс")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 4:
                        add_to_cart("Киткат")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 5:
                        add_to_cart("Кока-кола")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 6:
                        add_to_cart("Энергетик Берн")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 7:
                        add_to_cart("Твикс")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 8:
                        add_to_cart("Энергетик Редбулл")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 9:
                        add_to_cart("Шипучка")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 10:
                        add_to_cart("Чипсы крабовые")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 11:
                        add_to_cart("Чипсы крабовые")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 12:
                        add_to_cart("Чипсы крабовые")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 13:
                        add_to_cart("Чипсы крабовые")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    elif nomerproducta == 14:
                        add_to_cart("Чипсы крабовые")

                        eshyoproduct = int(input("Хотите что-нибудь еще? 1 - Да, 2 - Нет: "))
                        if eshyoproduct == 1:
                            prod2 = 1
                        elif eshyoproduct == 2:
                            prod2 = 0
                        else:
                            print('Вы ввели что-то не то')

                    else:
                        print("Вы ввели что-то не то")
                    
                    total_price = calculate_total(cart)
                    print(f"Стоимость корзины: {total_price} рублей.")

            elif vibor == 3:

                class ReviewSystem:
                    def __init__(self):
                        self.reviews = []

                    def add_review(self, text, rating):
                        review = {'text': text, 'rating': rating}
                        self.reviews.append(review)
                        print("Отзыв добавлен: ")

                    def remove_review(self, index):
                        if 0 <= index < len(self.reviews):
                            removed_review = self.reviews.pop(index)
                            print(f"Отзыв удален: {removed_review}")
                        else:
                            print("Некорректный индекс: ")

                    def display_reviews(self):
                        if not self.reviews:
                            print("Нет отзывов для отображения.")
                        else:
                            for index, review in enumerate(self.reviews):
                                print(f"{index + 1}. {review['text']} (Оценка: {review['rating']})")


                otziv = int(input("Выберите что хотите сделать: 1 - Добавить отзыв, 2 - Удалить отзыв, 3 - Посмотреть все отзывы: "))

                if otziv == 1:
                    a = str(input("Введите текст отзыва: "))
                    b = int(input("Введите оценку отзыва: "))
                        
                    review_system = ReviewSystem()
                    review_system.add_review(f"{a}", b)

                elif otziv == 2:
                    review_system = ReviewSystem()
                    review_system.remove_review(0)
                    print("Отзыв удален")

                elif otziv == 3:
                    review_system.display_reviews()

            elif vibor == 4:
                for computer in computers:
                    print(f"Название: {computer['title']}, Количество компьютеров: {computer['colvocomputers']}, Рейтинг: {computer['rating']}, Цена: {computer['price']}, Часы работы: {computer['vchas']}")
                def create_order():
                    
                    hall_number = int(input("Введите номер зала (1-10): ")) - 1
                    hours = int(input("Введите количество часов (максимум 20): "))
                    
                    if hall_number < 0 or hall_number >= len(computers):
                        print("Неверный номер зала.")
                        return
                    
                    if hours < 1 or hours > 20:
                        print("Количество часов должно быть от 1 до 20.")
                        return
                    
                    total_price = computers[hall_number]['price'] * hours
                    print(f"Стоимость заказа: {total_price} рублей")

                create_order()

            elif vibor == 5:
                print ("Вы вышли. Всего доброго!")
                prod1 = 0

    elif (otvet1 == 2 and ar == 1):
        print ("Вы зашли за админа ")
        prodadm = 1
        while (prodadm == 1):
            print ("Панель функций ")
            print ("Выберите действие:")
            print ("    1. Ввести новый зал в эксплутацию")
            print ("    2. Дополнить список товаров")
            print ("    3. Уволиться")
            print ("    4. Выйти")

            viboradm = int((input()))

            if (viboradm == 1): 
                new_nomer_zala = str(input("Введите номер нового зала(буквами): "))
                new_colvo_comp = int(input("Введите количество компьютеров в новом зале: "))
                new_tsena = int(input("Введите новую цену: "))
                new_chasi = int(input("Введите количество часов: "))

                new_room = {f'title': new_nomer_zala, 'colvocomputers': new_colvo_comp, 'rating': "-", 'price': new_tsena, 'vchas': new_chasi}
                computers.append(new_room)
                prod = 1

            elif (viboradm == 2): 
                new_t_product = str(input("Введите название нового продукта: "))
                new_tsena1 = int(input("Введите новую цену: "))
                
                new_product = {f'name': new_t_product, 'price': new_tsena1}
                products.append(new_product)

            elif (viboradm == 3): 
                admin.pop("login", None)  
                del admin["parol"]  
                print("Вы уволились") 

            elif (viboradm == 4): 
                prodolzh = 1
                prodadm = 0

            else:
                print ("Вы ввели что-то не то ")
                prod = 1
    
else:
    print ("Вы не смогли зарегистрироваться, начните заного")
