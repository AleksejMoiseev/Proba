#!/usr/bin/env python3
"""
1. Создать базовый класс «Домашнее животное» и производные классы
«Собака», «Кошка», «Попугай», «Хомяк». С помощью конструктора
установить имя каждого животного и его характеристики. Реализуйте для
каждого из классов методы:
Sound — издает звук животного (пишем текстом в консоль)
Show — отображает имя животного;
Type — отображает название его подвида

"""
from abc import ABC, abstractmethod


class HomeAnimal(ABC):

    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        self._color = val

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def sound(self):
        pass

    def show(self):
        print(f"Имя животного{self._name}")
        return self._name

    def __str__(self):
        return f"Name home animal : {self._name};  Color:  {self._color}; " \
               f"Подкласс : "


class Cat(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name=name, color=color)

    @staticmethod
    def sound():
        return "Мяу Мяу"

    @staticmethod
    def type():
        return "Млекопитающиеся"


class Dog(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name=name, color=color)

    @staticmethod
    def sound():
        return "Гав Гав"

    @staticmethod
    def type():
        return "Млекопитающиеся"


class Hamster(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name=name, color=color)

    @staticmethod
    def sound():
        return "Хрум Хрум"

    @staticmethod
    def type():
        return "Млекопитающиеся"


class Parrot(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name=name, color=color)

    @staticmethod
    def sound():
        return "Кар Кар"

    @staticmethod
    def type():
        return "Птица"


def main():
    myrka = Cat("Мурка", "White")
    sharik = Dog(name="Шарик", color="Серо-буро-малиновый")
    dysya = Hamster(name="Дуся", color="Коричневый")
    kesha = Parrot(name="Инокентий", color="Разноцветный")
    print(myrka, myrka.type(), "сказала", myrka.sound())
    print(sharik, sharik.type(), "сказала", sharik.sound())
    print(dysya, dysya.type(), "сказала", dysya.sound())
    print(kesha, kesha.type(), "сказала", kesha.sound())


if __name__ == '__main__':
    main()
