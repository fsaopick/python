#ucheniki = { "Альберт", "Ваня", "Юлий", "Нурлан" }
#ucheniki1 = { "Юля", "Катя", "Саша", "Даша", "Ваня"}

#union_set =  ucheniki | ucheniki1 #names.union(ucheniki1)
#print (union_set)

#print(ucheniki.intersection(ucheniki1)) #пересечение
#print (ucheniki & ucheniki1)

#print(ucheniki.difference(ucheniki1)) #разность в одном множестве - убирает то что есть во 2 множестве 
#print(ucheniki - ucheniki1)

#print(ucheniki.symmetric_difference(ucheniki1))   #разность в одном множестве - убирает то что есть и там и там 
#print(ucheniki ^ ucheniki1)

#словари 

stundent = {
    "name": "Вася",
    "age": "15",
    "group": "p-5-23",
}

print(stundent) #вывод всего словаря
stundent["name"] = "Петя" #замена в ключе чего-либо
print(stundent["name"]) #вывод по ключу
print(stundent["age"])
print(stundent["group"])

stundent["city"] = "Moscow" #добавление новой пары ключ - значение в словарь
print(stundent)

#del stundent["age"] #удаление пары ключ - значение 
#print(stundent)

element = stundent.pop("name") #вывод значения через ключ
print(element)
print(stundent)

#stundent.clear() #очищение словаря
#print(stundent)

print(stundent.get("name", "Неизвестое значение")) # вывод значения по ключу, по дефолту - неизвестное, если пустое
print(list(stundent.keys())) #все ключи
print(list(stundent.values())) #значения всех ключей
print(list(stundent.items())) #получение всех пар в форме кортежей 

stundent.update({"point": 5, "surname": "Иванов" })
print(stundent)

group = {
    "Петя": {
        "point": 5, 
        "course": "Русский"
    },
    "Катя": {
        "point": 4, 
        "course": "Математика"
    }
}

print(group["Петя"]["course"])

for i in stundent:
    print("Ключ: ", i, ", значение: ", stundent[i])


for key, value in stundent.items():
    print(key, value)