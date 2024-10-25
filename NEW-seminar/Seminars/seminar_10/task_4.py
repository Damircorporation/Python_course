# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Person:
    person_list = []

    def __init__ (self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self._age = age
        self.city = city
        Person.person_list.append(self)

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self._age

    def get_city(self):
        return self.city

class Worker(Person):
    def __init__(self, id_worker, name, surname, age, city):
        super().__init__(name, surname, age, city)
        if 100_000 <= id_worker <= 999_999:
            self.id_worker = id_worker
        else:
            self.id_worker = 100_000
        self.guard = self.id_worker % 7

    def get_level_guard(self):
        return self.guard

if __name__ == '__main__':
    p1 = Worker(123456, 'Alex', 'Smit', 23, 'London')
    print(p1.guard)
    print(p1.get_level_guard())
    print(p1.name)
