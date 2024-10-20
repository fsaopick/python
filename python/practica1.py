import random

print ("Вступительные испытания для работа во Вкусно-и-точка")

print ("Как будут звать вашего героя?")

rabotnik = {
    "name": "",
    "age": "",
    "cfalifik": "",
}

rabotnik["name"] = str(input("Введите имя: ")) 

rabotnik["age"] = int(input("Введите возраст: ")) 

rabotnik["cfalifik"] = int(input("Введите специализацию вашего героя: 1 - бургеры, 2 - картошка, 3 - напитки: ")) 

print ("Вы создали вашего героя")

cfalifik1 = rabotnik.pop("cfalifik")
age = rabotnik.pop("age")

if cfalifik1 == 1 and 16 <= age < 50:
    print("")
    print("Для того, чтобы взять Вас на работу, вам необходимо выполнить 3 заказа")

    tuple_burg = ("1 заказ - вам необходимо сделать гамбургер", "2 заказ - вам необходимо сделать картофель средний", "3 заказ - вам необходимо налить напиток - Добрый кола")

    print(tuple_burg[0])
    print("Для изготовления бургера вам дается технологическая карта: состав гамбургера: булочка, котлетка, помидор, лук, соленья, бекон - 7 продуктов")

    otvet = int(input("Замечаете ли вы странность в этой карте? 1 - Да, 2 - Нет: "))
    if otvet == 1:
         print("")
         print("Вы заметили, что в технологической карте есть проблема - не хватает одного продукта")

         print("Сначала введите цифры продуктов, которые вы возьмете из доступных по технологичсекой карте: ")
         list_producti= ["булочка","котлетка","салат","картошка","капуста", "помидор", "соленья", "бекон", "лук", "морковь","сыр"]
         print(list_producti)

         a = list_producti.pop(int(input("Первый продукт: ")) - 1)
         list_user = []
         list_user.append(a)

         b = list_producti.pop(int(input("Второй продукт: ")) - 1)
         list_user.append(b)

         c = list_producti.pop(int(input("Третий продукт: ")) - 1)
         list_user.append(c)

         d = list_producti.pop(int(input("Четвертый продукт: ")) - 1)
         list_user.append(d)

         e = list_producti.pop(int(input("Пятый продукт: ")) - 1)
         list_user.append(e)

         r = list_producti.pop(int(input("Шестой продукт: ")) - 1)
         list_user.append(r)

         dop_prod = (input("Какого продукта не хватает?(скорее всего, этот продукт находится в доступных продуктах) - ")) 
         list_user.append(dop_prod)
         
         print(list_user)
         
    else:
         print("Введите цифры продуктов, которые вы возьмете из доступных: ")
         list_producti = ["булочка","котлетка","салат","картошка","капуста", "помидор", "соленья", "бекон", "лук", "морковь","сыр"]
         print(list_producti)

         a = list_producti.pop(int(input("Первый продукт: ")) - 1)
         list_user = []
         list_user.append(a)

         b = list_producti.pop(int(input("Второй продукт: ")) - 1)
         list_user.append(b)

         c = list_producti.pop(int(input("Третий продукт: ")) - 1)
         list_user.append(c)

         d = list_producti.pop(int(input("Четвертый продукт: ")) - 1)
         list_user.append(d)

         e = list_producti.pop(int(input("Пятый продукт: ")) - 1)
         list_user.append(e)

         r = list_producti.pop(int(input("Шестой продукт: ")) - 1)
         list_user.append(r)

         print(list_user)

    proverka_sost = ["булочка", "лук", "котлетка", "помидор", "соленья", "бекон", "салат"]
    list_user.sort()

    itog = all(elem in list_user for elem in proverka_sost)

    if itog == True:
         print("Вы собрали все по технологической карте - ваш бургер идет на поднос и отдается посетителю")
         print("Посетителю все понравилось - вы успешно выполнили 1 заказ")
         
    predup_list = []

    if itog == False:
        print("Вы что-то выбрали не то или у вас не достает ингридиентов")

        vezenie = {1, 2, 3, 4}
        random_index = random.randrange(0, len(vezenie))
        popped_elem = list(vezenie)[random_index]

        if popped_elem == 1 or popped_elem == 3:
            print("Посетитель не заметил, что что-то не так")
            
        if popped_elem == 2 or popped_elem == 4:
            print("Посетитель заметил, что в бургере что-то не так, вам делают преупреждение")
        predup_list.append(1) 

    print("")
    print(tuple_burg[1])
    print("Для приготовления картофеля вам необходимо выполнить несколько простых шагов: 1) взять  полуфабрикат 2) приготовить в масле картофель 3) положить картофель в упаковку и посолить")
    print("Вы взяли полуфабркат и положили его в масло")
    vremya = int(input("Сколько времени вы будете держать полуфабрикат в масле?: "))
    print("Далее Вы солите картофель и отдаете его")

    if vremya == 5:
        print("Посетителю все понравилось - Вы успешно выполнили заказ")
    else:
        ("Вы выбрали неправильное время для приготовления")
        vezenie = {1, 2, 3, 4}
        random_index = random.randrange(0, len(vezenie))
        popped_elem = list(vezenie)[random_index]

        if popped_elem == 1 or popped_elem == 3:
            print("Вам повезло и посетитель не стал жаловаться")
            
        if popped_elem == 2 or popped_elem == 4:
            print("Вам не повезло и посетитель стал жаловаться - вам дали предуреждение")
            predup_list.append(2)

    print("")
    print(tuple_burg[2])
    print("Чтобы налить колу вам необходимо выбрать правильный кулер - номер, номера кулеров идут строго по порядку")

    napitok = int(input("1 - фанта, 2 - спрайт, 3 - пепси, 4 - Добрый кола: "))

    if napitok == 4:
        print("Вы успешно выполнили заказ")
    else:
        vezenie = {1, 2, 3, 4}
        random_index = random.randrange(0, len(vezenie))
        popped_elem = list(vezenie)[random_index]

        if popped_elem == 1 or popped_elem == 3:
            print("Вам повезло и посетитель не стал жаловаться")
            
        if popped_elem == 2 or popped_elem == 4:
            print("Вам не повезло и посетитель стал жаловаться - вам дали предуреждение")
            predup_list.append(3)

    predup = len(predup_list)

    if predup == 3 or predup == 2:
        print("Вы не смогли ничего выполнить - вас не берут на работу")
    else:
        print("Вас берут на работу ")
        


else:
    print("")
    print("Вас не могут взять по техническим причинам - скорее всего, вы выбрали квалификацию отличную от 1 - на ней много работников, либо Вы ввели некорректный возраст - запустите игру заново с другими данными")
