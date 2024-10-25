# Задание №1
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# def user_input(text):
#     words = sorted(text.split())
#     max_lenght = len(max(words, key=len))
#     print(words)
#     print(max(words))
#     print(max(words, key=len))
#     print(max_lenght)
#     for i, word in enumerate(words, start=1):
#         print(f'{i}. {word:>{max_lenght}}')
#
#
# input_text = input('Введите текст: ')
# user_input(input_text)



# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def unique_unicode(text: str) -> list[int]:
#     set_letters = sorted(set(text), reverse=True)
#     return list(map(ord, set_letters))
#
#
# text_out = input('Введите текст: ')
# print(*unique_unicode(text_out))



# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def user_input_str(text: str) -> dict[str, int]:
#     start, stop = sorted(map(int, text.split()))
#     my_dict = {}
#     for key in range(start, stop + 1):
#         my_dict[chr(key)] = key
#     return my_dict
#
#
# input_text = input('Введите строку: ')
# print(user_input_str(input_text))



# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# def bubble_sort(list_1: list[int]):
#     for i in range(1, len(list_1)):
#         is_sorted = True
#         for j in range(len(list_1)-1):
#             if list_1[j] > list_1[j+1]:
#                 list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
#                 is_sorted = False
#         if is_sorted:
#             return
#
#
# new_list = [1, 5, 9, 20, 3, 89, 61, 11]
# print(new_list)
# bubble_sort(new_list)
# print(new_list)


# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

# def salary(names: list[str], base_salary: list[str], percent: list[str]) -> dict[str, int]:
#     my_dict = {}
#     for name, bases, proc in zip(names, base_salary, percent):
#         my_dict[name] = bases * float(proc[:-1]) / 100
#     return my_dict
#
#
# names_in = ['Ivan', 'Petr', 'Serg']
# base_salary_in = [100_000, 80_000, 120_000]
# percent_in = ['10.25%', '5.6%', '8%']
# print(salary(names_in, base_salary_in, percent_in))


# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка

# def user_input_str(arr, i, j):
#     i, j = sorted([i, j])
#     i = i if i > 0 else 0
#     j = j if j < len(arr) else len(arr) - 1
#     return sum(arr[i:j + 1])
#
#
# list_1 = [4, 5, 8, 1, 9, 3]
# index_one = int(input('Введите первый индекс: '))
# index_two = int(input('Введите второй индекс: '))
# print(user_input_str(list_1, index_one, index_two))


# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def func(user_data):
#     new_list = []
#     for v in user_data.values():
#         new_list.append(sum(v) > 0)
#
#         return all(map(lambda x: sum(x) >= 0, user_data.values()))
#
#
# data = {
#     "Рога": [42, -73, 12, 85, -15, 2],
#     "Копыта": [45, 25, -100, 22, 1],
#     "Хвосты": [-10, 123, 52, 45, 93],
# }
# print(func(data))


# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# def change_val():
#     variables = globals()
#     change = {}
#     print(variables)
#     for key, value in variables.items():
#         if key[-1] == 's' and key != 's':
#             change[key[:-1]] = value
#             change[key] = None
#     variables.update(change)
#
#
# datas = [42, -73, 12, 85, -15, 2]
# s = 'Hello world'
# names = ('NoName', 'OtherName', 'NewName')
# sx = 42
# change_val()
# print(globals())

# datas = None
# data = [42, -73, 12, 85, -15, 2]
# s = 'Hello world'
# names = None
# name = ('NoName', 'OtherName', 'NewName')
# sx = 42