# Задание 2. Преобразование числа в шестнадцатеричное представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

# # Примеры чисел
# numbers = [255, 16, 0, -42]
# # Определяем символы для цифр в шестнадцатеричной системе
# hex_digits = '0123456789ABCDEF'
# for number in numbers:
#     # Если число равно 0, то возвращаем '0'
#     if number == 0:
#         hex_string = '0'
#     else:
#         # Обрабатываем отрицательные числа
#         is_negative = number < 0
#         if is_negative:
#             number = -number
#         # Преобразование числа в шестнадцатеричное представление
#         hex_string = ''
#     while number > 0:
#         remainder = number % 16
#         hex_string = hex_digits[remainder] + hex_string
#         number //= 16
#     # Добавляем префикс '-' для отрицательных чисел
#     if is_negative:
#         hex_string = '-' + hex_string
#         print(hex_string)


# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.

# # Импортируем класс Fraction из модуля fractions
# from fractions import Fraction
# # Вводим первую дробь
# frac1 = input("Введите числа первой дроби (a/b): ")
# # Вводим вторую дробь
# frac2 = input("Введите числа второй дроби (a/b): ")
# # Разделяем строки и преобразуем числитель и знаменатель первой дроби в целые числа
# numerator1, denominator1 = map(int, frac1.split('/'))
# # Разделяем строки и преобразуем числитель и знаменатель второй дроби в целые числа
# numerator2, denominator2 = map(int, frac2.split('/'))
# # Создаем объекты Fraction для первой и второй дроби
# f1 = Fraction(numerator1, denominator1)
# f2 = Fraction(numerator2, denominator2)
# # Находим сумму дробей
# sum_frac = f1 + f2
# # Находим произведение дробей
# product_frac = f1 * f2
# # Выводим результат суммы дробей
# print("Сумма:", sum_frac)
# # Выводим результат произведения дробей
# print("Произведение:", product_frac)


