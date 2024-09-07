# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# РЕШЕНИЕ
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# indices = []
# for i in range(len(list_1)):
#     if min_number < list_1[i] < max_number:
#         indices.append(i)
# print("Индексы элементов, значения которых принадлежат диапазону от", min_number, "до", max_number, ":", indices)

# или так

# list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list)):
#     if min_number <= list[i] <= max_number:
#         print(i)



# Задача №30:
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# РЕШЕНИЕ
# a1 = 2
# d = 3
# n = 5
# def arithmetic_progression(a1, d, n):
#     progression = []
#     for i in range(1, n+1):
#         an = a1 + (i-1) * d
#         progression.append(an)
#     return progression
# result = arithmetic_progression(a1, d, n)
# for item in result:
#     print(item)
