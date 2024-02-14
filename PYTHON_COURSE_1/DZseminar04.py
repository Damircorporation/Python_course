# Задача №1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# РЕШЕНИЕ
n, m = int, input().split()

set1 = list(int, input().split())
set2 = list(int, input().split())

common_numbers = []

for num1 in set1:
    if num1 in common_numbers:
        continue
    for num2 in set2:
        if num1 == num2:
            common_numbers.append(num1)
            break

common_numbers.sort()

for num in common_numbers:
    print(num, end=' ')