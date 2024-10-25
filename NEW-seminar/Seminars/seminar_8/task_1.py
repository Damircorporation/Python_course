# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import csv
import json
from pathlib import Path

def file_to_jsom(file: Path):
    data = {}
    with open(file, 'r', encoding='utf=8') as f_read:
        for line in f_read:
            name, number = line.split(' _ ')
            data[name.capitalize()] = number
        print(data)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f_write:
        json.dump(data, f_write, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    file_to_jsom(Path('file_new.txt'))
