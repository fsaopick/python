print("ку")

# name = input("введите имя -") #"petya"
# age = int(input("введите возраст - "))   #float(13)
# point = float(input("введите оценку - "))  #(4.5)
# is_active = bool(input("введите активность - "))

# print(name, age, point, is_active)

# print(int(point))
# print(age + point)


# a = input("введите числовое значение - "))
# b = input("введите числовое значение - "))

# # арифметические операторы 
# print ("сумма", a + b)
# print ("вычитание", a - b)
# print ("умножение", a * b)
# print ("деление", a / b)
# print ("деление нацело", a // b)
# print ("остаток от деления" - a % b)
# print ("степень", a ** b)

# # операторы сравнения 
# print (1 == 3)
# print (1 != 3)
# print (1 > 3)
# print (1 < 3)
# print (1 >= 3)
# print (1 <= 3)

# # логические операторы
# print (1 == 3) and print (1 != 3)
# print (1 == 3) or print (1 != 3)
# print (not(1 == 3))

# # операторы присваиванияф
# a = 5
# b = 3

# a += b       # a + b
# a -= b       # a - b
# a *= b       # a * b
# a /= b       # a / b
# print (a)





# 1. Дано трехзначное число. 
# Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).

# a = int(input("введите трехначное число"))
# b = a % 100
# c = b % 10
# d = b // 10
# v = a // 100

# print (v,c,d)


# 2.  Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, 
#  найти цифру, соответствующую разряду сотен в записи этого числа.

# a = int(input("введите трехначное число"))
# if a > 999:
#     a = a // 100
#     print(a)
# else:
#     print("x меньше 999")


# 3. Дано целое число. Вывести его строку-описание вида «отрицательное четное число», 
# «нулевое число», «положительное нечетное число» и т. д.

# a = int(input("введите трехначное число"))
# if a < 0: 
#     if a % 2 == 0:
#         print("отрицательное нечетное число")
#     else:
#         print("отрицательное четное число")
 
# elif a == 0:
#     print("число равно нулю")

# if a > 0: 
#     if a % 2 == 0:
#         print("положительно четное число")
#     else:
#         print("отрицательное четное число")
 



# 4. Арифметические действия над числами пронумерованы следующим образом: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление. 
# Дан номер действия N (целое число в диапазоне 1-4) и вещественные числа А и В (В не равно 0). 
# Выполнить над числами указанное действие и вывести результат.

a = int(input("введите первое число"))
b = int(input("введите второе число"))

print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")

x = int(input("выберите число действия"))
if x == 1:
    print(a + b)
elif x == 2:
    print(a - b)
elif x == 3:
    print(a * b)
elif x == 4:
    print(a / b)