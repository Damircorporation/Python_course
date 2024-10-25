# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.


from random import randint
from typing import Callable


def num_control(func, Callable):
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    COUNT_MIN = 1
    COUNT_MAX = 10

    def wrapper(num, count, *args, **kwargs):
        if num < NUMBER_MIN or num > NUMBER_MAX:
            num = randint(NUMBER_MIN, NUMBER_MAX)
        if count < COUNT_MIN or num > COUNT_MAX:
            num = randint(COUNT_MIN, COUNT_MAX)
        return func(num, count, *args, **kwargs)

    return wrapper


@num_control
def num_endeavors(num, count):
    for i in range(count):
        user_input_num = int(input('Введите число от 1 до 100: '))
        print(f'Оставшееся количество попыток - {count - i}')
        if user_input_num == num:
            print(f'Поздравляю число угадано - {num}, за {i} попыток')
        elif user_input_num > num:
            print('Загаданое число меньше!')
        elif user_input_num < num:
            print('Загаданое число больше!')
    return 'Ваши попытки закончились'


if __name__ == '__main__':
    print(num_endeavors(500, 5))
