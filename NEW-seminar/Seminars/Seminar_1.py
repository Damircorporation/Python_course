# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число. Откажитесь от магических чисел
# В коде должны быть один input и один print

# LOWER_LIMIT = 1
# UPPER_LIMIT = 999
# ONE = 1
# TEN = 10
# HUNDRED = 100
# num = LOWER_LIMIT - ONE
# while num < LOWER_LIMIT or num > UPPER_LIMIT:
#     num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}  '))
# if num < TEN:
#     result = f'Число {num} - число. Её квадрат равен {num * num}'
# elif num < HUNDRED:
#     prod = (num // TEN) * (num % TEN)
#     result = f'Число {num} - двузначное. произведение цифр равно {prod}'
# else:
#     first = num // HUNDRED
#     second = num // TEN % TEN
#     third = num % TEN
#     mirror = third * HUNDRED + second * TEN + first
#     result = f'Число {num} - трехзначное. Его зеркальное число равно {mirror}'
# print(result)



# Задание №8
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

# SPACE = " "
# STAR = "*"
# ONE = 1
# rows = int(input("Сколько рядов у елки?"))
# spaces = rows - ONE
# stars = ONE
# for _ in range(rows):
#     print(SPACE * spaces + STAR * stars)
#     stars += 2
#     spaces -= 1



# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как
# на школьной тетрадке.

# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMNS = 4
# for seed_first_num in (LOWER_LIMIT, LOWER_LIMIT+COLUMNS):
#     for second_num  in range(LOWER_LIMIT, UPPER_LIMIT+1):
#         for first_num in range(seed_first_num, seed_first_num+COLUMNS):
#             print (f'{first_num} x {second_num} = {first_num * second_num}', end='\t \t')
#         print()
#     print()

