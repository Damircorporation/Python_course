# Задание 1. Апгрейд калькулятора
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.

# def digits_summ(num):
#     # Функция для вычисления суммы цифр числа
#     summ = 0
#     while num > 0:
#         digit = num % 10  # Получаем последнюю цифру
#     summ += digit  # Добавляем цифру к сумме
#     num //= 10  # Удаляем последнюю цифру из числа
#     print('Сумма цифр:', summ)
#
# def max_digit(num):
# # Функция для нахождения максимальной цифры числа
#     maximum = 0
#     while num > 0:
#         digit = num % 10  # Получаем последнюю цифру
#         if digit > maximum:  # Сравниваем с текущим максимумом
#             maximum = digit  # Обновляем максимум
#         num //= 10  # Удаляем последнюю цифру из числа
#     print('Максимальная цифра:', maximum)
#
# def min_digit(num):
# # Функция для нахождения минимальной цифры числа
#     minimum = num % 10  # Начинаем с последней цифры
#     while num > 0:
#         digit = num % 10  # Получаем последнюю цифру
#         if digit < minimum:  # Сравниваем с текущим минимумом
#             minimum = digit  # Обновляем минимум
#         num //= 10  # Удаляем последнюю цифру из числа
#     print('Минимальная цифра:', minimum)
# # Основной цикл программы
# while True:
#     num = int(input('Введите число: ')) # Запрос числа у пользователя
#     action = int(input('Введите номер действия: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: ')) # Запрос действия
#     if action == 1:
#         digits_summ(num) # Вызов функции для суммы цифр
#     elif action == 2:
#         max_digit(num) # Вызов функции для максимальной цифры
#     elif action == 3:
#         min_digit(num) # Вызов функции для минимальной цифры
#     else:
#         print('Ошибка: неверная команда.') # Обработка неверного ввода


# Задача 2. Недоделка
# Вы пришли на работу в компанию по разработке игр, целевая аудитория —
# дети и их родители. У предыдущего программиста было задание сделать две
# игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не
# успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
# число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит, победил он или проиграл. Камень бьёт
# ножницы, ножницы режут бумагу, бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число
# до тех пор, пока он не отгадает загаданное.

# def rock_paper_scissors():
# """
# Функция для игры «Камень, ножницы, бумага».
# Пользователь выбирает вариант, и программа определяет результат
# игры.
# """
# # Запрос выбора пользователя
# player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: "))
# # Варианты выбора компьютера для примера
# computer = 1 # В этом примере компьютер всегда выбирает камень
# # Определение и вывод результата игры
# if player == computer:
#     print("Ничья!")
# elif (player == 1 and computer == 2) or (player == 2 and
#     computer == 3) or (player == 3 and computer == 1):
#     print("Вы выиграли!")
# elif (player == 1 and computer == 3) or (player == 2 and
# computer == 1) or (player == 3 and computer == 2):
#     print("Вы проиграли!")
# else:
#     print("Неверная команда. Попробуйте снова.")
#
#
# def guess_the_number():
# """
# Функция для игры «Угадай число».
# Пользователь пытается угадать загаданное число.
# """
# number = 7 # Загаданное число для примера
# while True:
#     # Запрос числа от пользователя
#     guess_num = int(input('Введите число: '))
#     # Проверка и вывод подсказки
#     if guess_num > number:
#         print('Число больше, чем нужно. Попробуйте ещё раз!')
#     elif guess_num < number:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print('Поздравляю, вы угадали! Возврат в главное меню.')
#         break # Выход из цикла, если число угадано
#
# def main_menu():
# """
# Главное меню, позволяющее пользователю выбрать игру или выйти из
# программы.
# """
# while True:
#     # Вывод меню выбора игры
#     print('Во что хотите поиграть?')
#     game = int(input('1 - Камень, ножницы, бумага; 2 - Угадай число; 3 - Выйти: '))
#     # Вызов соответствующей функции в зависимости от выбора
#     if game == 1:
#         rock_paper_scissors()
#     elif game == 2:
#         guess_the_number()
#     elif game == 3:
#         print('Выход из программы.')
#         break # Выход из цикла и завершение программы
#     else:
#         print('Неверная команда. Попробуйте снова.')
#     # Запуск главного меню
#     main_menu()


# Задача 3. Число наоборот
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.

# def reversal(x):
# # Инициализация переменных:
# # count будет использоваться для отслеживания количества цифр в числе
# # revers_x будет хранить перевёрнутое число
#     count = 0
#     revers_x = 0
#     # Подсчёт количества цифр в числе x
#     # Преобразуем число в строку и проходим по каждому символу (цифре)
#     for _ in str(x):
#         count += 1
#     # Переворачивание числа
#     while x > 0:
#     # Уменьшаем значение count на 1 на каждой итерации
#         count -= 1
#     # Получаем последнюю цифру числа x с помощью x % 10
#     # Добавляем эту цифру в перевёрнутое число (revers_x)
#     # Умножаем цифру на 10 в степени count для правильного размещения
#         revers_x += (x % 10) * (10 ** count)
#     # Удаляем последнюю цифру из x, деля его на 10
#     x = x // 10
# # Возвращаем перевёрнутое число
#     return revers_x
# # Ввод первого числа от пользователя
# num_1 = int(input('Введите первое число: '))
# # Ввод второго числа от пользователя
# num_2 = int(input('Введите второе число: '))
# # Применение функции reversal к первому числу
# revers_num1 = reversal(num_1)
# # Применение функции reversal ко второму числу
# revers_num2 = reversal(num_2)
# # Вывод перевёрнутого первого числа
# print('\nПервое число наоборот:', revers_num1)
# # Вывод перевёрнутого второго числа
# print('Второе число наоборот:', revers_num2)
# # Сложение перевёрнутых чисел
# amount = revers_num1 + revers_num2
# # Переворачивание суммы
# revers_summ = reversal(amount)
# # Вывод суммы перевёрнутых чисел
# print('\nСумма:', amount)
# # Вывод перевёрнутой суммы
# print('Сумма наоборот:', revers_summ)


# Задача 4. Функция максимума
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:

# def max_of_2(number_1, number_2):
# # Подсказка №2
# # Возвращает большее из двух чисел
#     if number_1 > number_2:
#         return number_1
#     return number_2
#
# def max_of_3(number_1, number_2, number_3):
# # Подсказка №3 и №4
# # Использует max_of_2 для нахождения максимума из трёх чисел
# # Сначала находит максимум из первых двух чисел
# # Затем находит максимум между результатом и третьим числом
#     return max_of_2(max_of_2(number_1, number_2), number_3)
# # Подсказка №5
# # Ввод трёх чисел от пользователя
# digit_1 = int(input('Введите первое число: '))
# digit_2 = int(input('Введите второе число: '))
# digit_3 = int(input('Введите третье число: '))
# # Вывод самого большого числа
# print('Самое большое число:', max_of_3(digit_1, digit_2, digit_3))


# Задача 5. Яйца
# В рамках программы колонизации Марса компания «Спейс Инжиниринг»
# вывела особую породу черепах, которые, по задумке, должны размножаться,
# откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к
# поверхности опасно из-за радиации, а слишком глубоко — из-за давления
# грунта и недостатка кислорода. Вообще, факторов очень много, но
# специалисты проделали большую работу и предположили, что уровень
# опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 −
# 12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в
# условных единицах. Для тестирования гипотезы нужно взять пробу грунта на
# безопасной, согласно формуле, глубине.
# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода.

# def calculate_danger(x):
#     """Функция для расчета уровня опасности по формуле."""
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
#
# def find_safe_depth(max_danger):
#     """Функция для нахождения глубины, при которой уровень опасности
# близок к нулю."""
#     d_min = 0
#     d_max = 4
#     d_middle = (d_min + d_max) / 2
#     middle_danger = calculate_danger(d_middle)
#     while abs(middle_danger) > max_danger:
#         if middle_danger > 0:
#             d_min = d_middle
#         else:
#             d_max = d_middle
#         d_middle = (d_min + d_max) / 2
#         middle_danger = calculate_danger(d_middle)
#     return d_middle
#
# def main():
#     """Основная функция для управления программой и ввода данных."""
#     max_danger = float(input('Введите допустимый уровень опасности:'))
#     if max_danger < 0:
#         print('Вы ввели недопустимое значение! Попробуйте еще раз.')
#     else:
#         safe_depth = find_safe_depth(max_danger)
#         print(f'Приблизительная глубина безопасной кладки: {safe_depth:.9f} м')





