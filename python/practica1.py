print ("Работа в мак")

print (" Как будут звать вашаго героя?")

rabotnik = {
    "name": "",
    "age": "",
    "cfalifik": "",
}

rabotnik["name"] = str(input("Введите имя")) 

rabotnik["age"] = str(input("Введите возраст")) 

rabotnik["cfalifik"] = int(input("Введите уровень подготовки вашего героя: 1 - начальный, 2 - средний, 3 - высокий")) 

cfalifik1 = rabotnik.pop("cfalifik")


if cfalifik1 == 1:
    print("52")
elif cfalifik1 == 2:
    print("522")
else:
    print("522")
