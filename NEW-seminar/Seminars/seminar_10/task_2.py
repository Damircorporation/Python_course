# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width == None:
            self.width = length
        else:
            self.width = width

    def perimetr(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

ticktack = Rectangle(2, 6)

print(f'{ticktack.perimetr = }')
print(f'{ticktack.area = }')