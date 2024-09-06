# Задача №1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# РЕШЕНИЕ
# var1 = '5 5'
# var2 = '50 2 30 4 10'
# var3 = '10 20 30 4 50'
# common_numbers = []
# # Разделяем строки на отдельные числа и преобразуем их в множества
# set_var2 = set(map(int, var2.split()))
# set_var3 = set(map(int, var3.split()))
# for num1 in set_var2:
#     if num1 in common_numbers:
#         continue
#     for num2 in set_var3:
#         if num1 == num2:
#             common_numbers.append(num1)
#             break
# common_numbers.sort()
# for num in common_numbers:
#     print(num, end=' ')



# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# РЕШЕНИЕ
arr = [5, 2, 6, 4, 9, 2, 7, 3]
max_berry_count = 0
max_berry_position = -1
for i in range(len(arr)):
    current_berry_count = arr[i] + arr[(i+1) % len(arr)] + arr[(i-1) % len(arr)]
    if current_berry_count > max_berry_count:
        max_berry_count = current_berry_count
        max_berry_position = i
print("Максимальное количество собранных ягод:", max_berry_count)
print("Позиция куста, с которого собрано максимальное количество ягод:", max_berry_position)