# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию.

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def date_check(date: str) -> bool:
    day, month, year = (int(item) for item in date.split('.'))
    if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if is_leap(year) and month == 2 and day > 29:
        return False
    if not is_leap(year) and month == 2 and day > 28:
        return False
    return True

if __name__ == '__main__':
    print(date_check('31.12.2003'))