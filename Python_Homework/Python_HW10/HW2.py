#!/usr/bin/env python3
"""
Создайте класс «Дробь». Необходимо хранить в полях класса: числитель и
знаменатель. Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса. Также создайте
методы класса для выполнения арифметических операций (сложение,
вычитание, умножение, деление, и т.д.).
"""


class Fraction:

    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @property
    def denominator(self):
        try:
            if self._denominator == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Уважаемый гражданин, деление на ноль запрещено")
            return exit(1)
        else:
            return self._denominator

    @denominator.setter
    def denominator(self, val):
        try:
            if val == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Уважаемый гражданин, деление на ноль запрещено")
            return exit(1)
        else:
            self._denominator = val

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, val):
        self._numerator = val

    def __str__(self):
        return f" {self._numerator}\n" \
            f"---\n" \
            f" {self._denominator}"

    def __add__(self, other):
        x = self._numerator + other.numerator
        y = self._denominator + other.denominator
        return Fraction(numerator=x, denominator=y)


d = Fraction(1, 0)
d.denominator = 2
d1 = Fraction(1, 2)

