# Создайте список кортежей, где каждый кортеж содержит информацию о продажах (продукт, количество, цена). 
# Напишите код, который рассчитывает общую сумму продаж и выводит ее.

producti = { 
    ("молоко", 11, 10 ),
    ("хлеб", 15, 10),
    ("сушки", 10, 20),
    ("соль", 100, 30), 
    ("сахар", 100, 30), 
  }

def  rasschet_itog_stoimost(producti): 
    itog_stoimost = 0

    for product, colichestvo, stoimost in producti:
        itog_stoimost += colichestvo * stoimost 
    return itog_stoimost

itog_stoimost = rasschet_itog_stoimost(producti)
print(itog_stoimost)