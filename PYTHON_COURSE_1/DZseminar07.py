# Задача №1 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# РЕШЕНИЕ

# stroka = "если-я-чушу в-затылке-не-беда"
# lines = stroka.split()
# print(lines)
# lst = [sum(x in 'уеыаоэяию' for x in lin)
#  for lin in lines]
# if len(set(lst)) == 1 :
#     res = "Парам пам-пам"  
# else: res = "Пам парам"
# print(res)

# Получаем стихотворение от пользователя
stroka = input("Введите стихотворение Винни-Пуха: ")
# Разбиваем стихотворение на фразы
phrases = stroka.split()
# for i in phrases:
#     if phrases[i] == 1:
#          print("Количество фраз должно быть больше одной!")
# Функция для подсчета количества гласных букв в фразе
count_vowels = lambda phrase: sum(1 for letter in phrase if letter.lower() in 'aeiouаеёиоуыэюя')
# Подсчитываем количество гласных в каждой фразе
syllable_counts = [count_vowels(phrase) for phrase in phrases]
# Проверяем, одинаково ли количество гласных во всех фразах
if all(count == syllable_counts[0] for count in syllable_counts):
    print("Парам пам-пам")
else:
    print("Пам парам")

# Задача №2 Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# РЕШЕНИЕ 

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(operation(i, j), end=' ')
#         if i < num_rows:
#             print()
# print_operation_table(lambda x, y: x * y, 4, 5)



# def operation(i, j):
#     return i * j
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     table = []
#     for i in range(1, num_rows + 1):
#         row = []
#         for j in range(1, num_columns + 1):
#             row.append(operation(i, j))
#         table.append(row)
#     return table

# result_table = print_operation_table(operation, 3, 5)
# for row in result_table:
#     print(row)
# # print_operation_table(lambda x, y: x * y, 4, 5)