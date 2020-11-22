#!/usr/bin/env python3
"""
Реализовать класс Writer(first_name, last_name, birth_year). Все атрибуты
read only.
"""


class Writer:
    def __init__(self, first_name, last_name, birth_year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_year = birth_year

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def birth_year(self):
        return self.__birth_year


if __name__ == '__main__':
    writer1 = Writer(first_name="Ivanov", last_name="ivan", birth_year=1934)
    print(writer1.first_name)
    print(writer1.last_name)
    print(writer1.birth_year)