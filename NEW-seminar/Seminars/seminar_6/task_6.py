# Задание №6
# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.


_data = {}


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
               'Сидит дед во сто шуб одет': ['лук', 'луковица']}
    # print(puzzles.items())
    for key, value in puzzles.items():
        result = riddle(key, value, 3)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
        save(key, result)


def save(puzzle, count):
    _data[puzzle] = count
    # _data.update({puzzle: count})
    # _data.setdefault(puzzle, count)


def show():
    res = (
        f'Угадал загадку "{key}" с {value} попытки' if value > 0
        else f'Загадку "{key}"не угадал!'
        for key, value in _data.items()
    )
    print(*res, sep='\n')
    # print('\n'.join(res))


if __name__ == '__main__':
    storage()
    show()