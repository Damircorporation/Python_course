# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Bird:

    def __init__(self, name, age, weight, wing_span, beak_size):
        self.name = name
        self.age = age
        self.weight = weight
        self. wing_span = wing_span
        self. beak_size = beak_size

    def specific_bird(self):
        return f'Специфические особенности: {self.wing_span}, {self.beak_size}'


class Mammal:

    def __init__(self, name, age, weight, size, fangs):
        self.name = name
        self.age = age
        self.weight = weight
        self. size = size
        self. fangs = fangs

    def specific_animal(self):
        return f'Специфические особенности: {self.size}, {self.fangs}'


class Fish:

    def __init__(self, name, age, weight, depth, territory):
        self.name = name
        self.age = age
        self.weight = weight
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