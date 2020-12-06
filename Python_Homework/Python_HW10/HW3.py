#!/usr/bin/env python3
"""
Создайте базовый класс Shape для рисования плоских фигур. Определите
методы:
a. Show() — вывод на экран информации о фигуре;
b. Save() — сохранение фигуры в файл;
c. Load() — считывание фигуры из файла. Домашнее задание 1
Определите производные классы:
d. Square — квадрат, который характеризуется координатами левого
верхнего угла и длиной стороны;
e. Rectangle — прямоугольник с заданными координатами верхнего
левого угла и размерами;
f. Circle — окружность с заданными координатами центра и радиусом;

Создайте список фигур, сохраните фигуры в файл, загрузите в другой
список и отобразите информацию о каждой из фигур.
α
"""
import ast


class Shape:

    def __init__(self):
        self._dic = {'sideA': 0, 'sideB': 0, 'point': (0, 0), 'radius': 0, 'figure': 0}

    @property
    def variable_list(self):
        return self._dic

    def setter(self, **val):
        self._dic = val

    def show(self):
        counter = True
        print("*" * 50)
        for (key, value) in self._dic.items():
            if value != 0:
                print(f" Параметр: {key} имеет значение : {value}")
                counter = False
        if counter:
            print("Фигурой является точка в начале координат (0:0)")
        print("*" * 50)

    def save(self, mode=""):
        if mode == "":
            mode = "w+"
        text = str(self._dic) + "\n"
        with open("figure.txt", mode) as file:
            file.write(text)
        return text

    @staticmethod
    def load():
        with open("figure.txt", "r") as file:
            text = file.read()
        new_dict = ast.literal_eval(text)
        return new_dict


class Rectangle(Shape):

    def __init__(self, sideA, sideB):
        self._dic = {'figure': 'Rectangle', 'sideA': sideA, 'sideB': sideB}


class Square(Rectangle):

    def __init__(self, side):
        self._dic = {'figure': 'Square', 'sideA': side}


class Circle(Shape):

    def __init__(self, coordinateX, coordinateY, radius):
        self._dic = {'figure': 'Circle', 'point': (coordinateX, coordinateY), 'radius': radius}


def main():
    """
    Создание обьектов
    """
    rectangle = Rectangle(sideA=5, sideB=10)
    square = Square(side=5)
    circle = Circle(coordinateX=2, coordinateY=5, radius=10)
    """
    Создали лист из обьектов
    """
    start_list = [rectangle, square, circle]

    file = open("figure.txt", "w")
    file.close()
    """
    Записали обьекты в файл "figure.txt", предварительно его очистив
    """
    for obj in start_list:
        obj.save(mode="a")
    """
    Считываем фигуры в новый лист "end_list"
    """
    end_list = []
    with open("figure.txt", "r+") as  file:
        for line in file:
            line_dict = ast.literal_eval(line)
            end_list.append(line_dict)
    """
    Бежим по листу считывая фигуры   и демонстрируем обьекты
    """
    snape = Shape()
    for obj in end_list:
        snape.setter(**obj)
        snape.show()


if __name__ == '__main__':
    main()