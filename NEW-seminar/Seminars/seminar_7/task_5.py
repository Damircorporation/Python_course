# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import randint, choices
from string import ascii_lowercase, digits


def create_files(
        extension: str, min_name: int = 6, max_name: int = 30,
        min_size: int = 256, max_size: int = 4096, count: int = 3) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + '_' + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


def gen_files(**kwargs) -> None:
    # print(kwargs)
    for ext, counter in kwargs.items():
        create_files(extension=ext, count=counter)


if __name__ == '__main__':
    gen_files(bin=2, jpeg=1, txt=1)