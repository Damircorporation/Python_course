# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def riddle(secret, answers, qnty=3):
    print(f'Угадай загадку: {secret}')
    for tries in range(qnty + 1):
        answer = input('Введите ответ: ').lower()
        if answer in answers:
            return tries
    return 0

def storage():
    puzzles = {'Зимой и летом одним цветом': ['елка', 'ель', 'сосна'],
            'Не лает не кусает, а в дом не пускает': ['замок', 'домофон'],
              'Сидит дед во сто шуб одет': ['лук','луковица']}
    # print(puzzles.items())
    for key, value in puzzles.items():
        result = riddle(key, value, 3)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
if __name__ == '__main__':
    storage()