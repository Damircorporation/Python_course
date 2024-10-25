# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint

def num_riddles(num=randint(1,100), count=10):
    def num_endeavors():
        for i in range(1, count +1):
            user_input_num = int(input('Введите число от 1 до 100: '))
            print(f'Оставшееся количество попыток - {count - i}')
            if user_input_num == num:
                print (f'Поздравляю число угадано - {num}, за {i} попыток')
            elif user_input_num > num:
                print('Загаданое число меньше!')
            elif user_input_num < num:
                print('Загаданое число больше!')
        print(f'Ваши попытки закончились')
    return num_endeavors()

if __name__ == '__main__':
    func_num_game = num_riddles()
    print(func_num_game())

