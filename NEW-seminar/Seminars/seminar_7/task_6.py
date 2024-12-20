# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from os import chdir
from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path


def create_files(
        extension: str, min_name: int = 6, max_name: int = 30,
        min_size: int = 256, max_size: int = 4096, count: int = 3) -> None:
    for _ in range(count):
        while True:
            name = ''.join(choices(ascii_lowercase + '_' + digits, k=randint(min_name, max_name)))
            if not Path(f'{name}.{extension}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


def gen_files(path: str | Path, **kwargs) -> None:
    # print(kwargs)
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)
    for ext, counter in kwargs.items():
        create_files(extension=ext, count=counter)


if __name__ == '__main__':
    gen_files(bin=2, jpeg=1, txt=1)