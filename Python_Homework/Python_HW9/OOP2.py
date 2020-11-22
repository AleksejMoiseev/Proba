#!/usr/bin/env python3
"""
Создать класс Rectangle который конструируется с двумя аргументами
height и width. Следует имплементировать на Rectangle следующие методы:
○ area() - возвращает площадь
○ perimeter() - возвращает периметр
○ __str__()
○ класс метод clone() - создает копию текущего объекта и возвращает
новый объект
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    @classmethod
    def clone(cls, height, width):
        return cls(height=height, width=width)

    def __str__(self):
        print("  - прямоугольник -")
        return f" Длина {self.height} ед x Ширина {self.width} ед"


if __name__ == '__main__':
    rectangle1 = Rectangle.clone(height=2, width=2)
    print(f"Площадь прямоугольника 1 = {rectangle1.area} кв. ед ")
    print(f"Периметр прямоугольника 1 = {rectangle1.perimeter}  ед ")
    print(rectangle1)
