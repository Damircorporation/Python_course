# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки.

from os import chdir
from pathlib import Path
from pkgutil import extend_path


def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)

    if groups is None:
        groups = {
            Path('video'): ['avi', 'mkv'],
            Path('images'): ['ipg', 'png'],
            Path('audio'): ['mp3', 'wav', 'agg']
        }

    print(groups)
    reverse_groups = {}
    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        # print(target_dir, extension_list)
        for ext in extension_list:
            reverse_groups[f'.{ext}'] = target_dir
    print(reverse_groups)

    for file in path.iterdir():
        # print([file])
        # print(file.suffix)
        # print(file.name)
        if file.is_file() and file.suffix  in  reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)



if __name__ == '__main__':
    sort_files(Path(r'C:\Users\user\Desktop\Вся учеба\Учеба\Python_course\NEW-seminar'))