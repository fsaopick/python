# Напишите программу, которая создает список из 5 студентов с их оценками (имя и оценка как кортежи). 
# Позвольте пользователю добавить нового студента и его оценку.


ucheniki = { 
    ("Альберт", '5'),
    ("Ваня", '2'),
    ("Юлий", '3'),
    ("Нурлан", '4'), 
    ("Исмаил", '5'), 
    }


name = (input("Введите имя ученика - "))
ocenka = (input("Введите оценку ученика - "))

itog = (name, ocenka)
ucheniki.add(itog)

print(ucheniki)

