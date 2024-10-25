# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, choice
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghklzcdffmh'
MIN_LEN = 4
MAX_LEN = 7

def generate_names(filename: str | Path, names_count: int):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(names_count):
            name = ''
            cur_letter = choice((-1, 1))
            for _ in range(randint(MIN_LEN, MAX_LEN)):
                if cur_letter == -1:
                    name += choice(VOWELS)
                else:
                    name += choice(CONSONANTS)
                cur_letter *= -1
            f.write(name.capitalize() + '\n')

if __name__ == '__main__':
    generate_names(Path('name.txt'), 10)