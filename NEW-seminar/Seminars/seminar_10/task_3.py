# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

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

if __name__ == '__main__':
    p1 = Person('Alex', 'Smit', 23, 'London')
    p2 = Person('Oleg', 'Bobic', 28, 'Tokio')
    p3 = Person('Bob', 'Gaga', 35, 'Noscow')
    print(p1.person_list)
    print(p1.get_age())
    print(p1.full_name())




