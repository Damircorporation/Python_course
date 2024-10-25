# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from calendar import month


from random import randrange


def guess_the_numb(low_limit: int = 0, upper_limit: int = 100, try_limit: int = 10):
    user_number = int(input(f'Введите число от {low_limit} до {upper_limit}: '))
    rand_numb = randrange(low_limit, upper_limit + 1)
    counter = 1
    while counter <= try_limit:
        if user_number < rand_numb:
            return True
        elif user_number < rand_numb:
            user_number = int(input('Ваше число меньше загаданного, попробуйте еще раз: '))
        else:
            user_number = int(input('Ваше число больше загаданного, попробуйте еще раз: '))
        counter += 1
    return False


print(guess_the_numb(1, 10, 3))