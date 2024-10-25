# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


class Bird(Animal):

    def __init__(self, name, age, weight, wing_span, beak_size):
        super().__init__(name, age, weight)
        self. wing_span = wing_span
        self. beak_size = beak_size

    def specific_bird(self):
        return f'Специфические особенности: {self.wing_span}, {self.beak_size}'


class Mammal(Animal):

    def __init__(self, name, age, weight, size, fangs):
        super().__init__(name, age, weight)
        self. size = size
        self. fangs = fangs

    def specific_animal(self):
        return f'Специфические особенности: {self.size}, {self.fangs}'


class Fish(Animal):

    def __init__(self, name, age, weight, depth, territory):
        super().__init__(name, age, weight)
        self. depth = depth
        self. territory = territory

    def specific_fish(self):
        return f'Специфические особенности: {self.depth}, {self.territory}'

if __name__ == '__main__':
    p1 = Bird('сойка', '2', '0,5 кг', '30', '0,1 см')
    p2 = Mammal('тигр', '3', '25 кг', 'крупный', 'правда')
    p3 = Fish('окунь', '1', '0,35 кг', 'река', 'урал')

print(p1.specific_bird())
print(p2.specific_animal())
print(p3.specific_fish())
