# Задание №2
#  Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys
#
# data = [42, "Hello", 3.14, True, None, (1,2,3), "Hello", 123, 256, 2**8]
# for index, value in enumerate(data, start=1):
#     check_int = 'Это целое число' if isinstance(value, int) else ''
#     check_str = 'Это строка' if isinstance(value, str) else ''
#
#     print(f'порядковый номер: {index}, \t'
#           f'значение: {value}, \t'
#           f'адрес в памяти: {id(value)}, \t'
#           f'размер в памяти: {sys.getsizeof(value)}, \t'
#           f'хэш объекта: {hash(value)}, \t'
#           f'{check_int}{check_str}')


# Задание №3
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.

# ZERO = 0
# BIN = 2
# OCT = 8
#
# num_orig: int = int(input('Введите число '))
# for div in (BIN, OCT):
#     num = num_orig
#     result: str = ''
#
#     while num > ZERO:
#         result = str(num % div) + result
#         num //= div
#     print(result)
# print(bin(num_orig))
# print(oct(num_orig))


# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math
# import decimal
#
# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)
# d = input('Введите диаметр круга не превышающий 1000у.е\n')
# 
# while not d.isdigit() or int(d) > 1000 or int(d) < 1:
#     print('Число указанно некоректно')
#     d = input('Введите диаметр круга не превышающий 1000у.е\n')
#
# d = decimal.Decimal(d)
# area = PI * (d/2)**2
# length = PI * d
# print('Площадь круга', area)
# print('Длина окружности', length)


# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

# a = float(input('Введите значение a: '))
# b = float(input('Введите значение b: '))
# c = float(input('Введите значение c: '))
#
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b + d ** 0.5) / (2 * a)
#     result = f'У уравнения два корня: {x1 = } и {x2 = }'
# elif d == 0:
#     x1 = (-b) / (2 * a)
#     result = f'у уравнения два корня: {x1 = }'
# else:
#     d = complex(d,0)
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b + d ** 0.5) / (2 * a)
#     result = f'У уравнения два комплексных корня: {x1 = } и {x2 = }'
# print(result)


# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

ZERO = decimal.Decimal(0)
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MAX_REMOVAL = decimal.Decimal(600)
MIN_REMOVAL = decimal.Decimal(30)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER_4_PERCENTAGES = 3
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)

bank_account = ZERO
count = ZERO

while True:
    action = 1
    while action not in (CMD_DEPOSIT, CMD_WITHDRAW, CMD_EXIT):
        action = input(f'Введите:\n'
                       f'{CMD_DEPOSIT} = Пополнение\n'
                       f'{CMD_WITHDRAW} = Снятие\n'
                       f'{CMD_EXIT} = Выход\n')
        if action == CMD_EXIT:
            print(f'Заберите Вашу карту')
            print(f'Баланс Вашей карты {bank_account}')
            break
        if bank_account > RICHNESS_SUM:
            percent = bank_account * RICHNESS_PERCENT
            bank_account -= percent
            print(f'Вычтен налог за богатство - {RICHNESS_PERCENT}% в сумме {percent}')
            print(f'Баланс Вашей карты {bank_account}')
        amount = 1
        while amount % MULTIPLICITY != ZERO:
            amount = decimal.Decimal(input(f'Введите сумму кратную {MULTIPLICITY}: '))

        if action == CMD_DEPOSIT:
            count += 1
            bank_account += amount
            result = f'Пополнение карты на {amount}'
        elif action == CMD_WITHDRAW:
            percent = amount * PERCENT_REMOVAL
            percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
            amount_percent = amount + percent
            if bank_account >= amount_percent:
                count += 1
                bank_account -= amount_percent
                result = f'Снятие с карты - {amount}. Процент за снятие  - {PERCENT_REMOVAL} в сумме {percent}'
            else:
                result = f'Недостаточно средств. Сумма с комиссией {amount_percent}'
        if count % COUNTER_4_PERCENTAGES == ZERO:
            amount_percent = bank_account * PERCENT_DEPOSIT
            bank_account += amount_percent
            result = f'{result}\n Начислено {PERCENT_DEPOSIT}% за {COUNTER_4_PERCENTAGES} операции, в сумме {amount_percent}'
        print(result)
        print(f'Баланс карты - {bank_account}')









