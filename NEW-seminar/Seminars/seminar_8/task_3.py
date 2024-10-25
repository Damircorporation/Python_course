# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path

def json_to_csv(file):
    with open(file, 'r', encoding='utf=8') as f_reader:
        data = json.load(f_reader)

    rows = []
    for level, dict_id in data.items():
        for id, name in dict_id.items():
            rows.append({'level': level, 'id': id, 'name': name})
    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_writer:
        cvs_write = csv.DictWriter(f_writer, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)

if __name__ == '__main__':
    json_to_csv(Path('users.json'))