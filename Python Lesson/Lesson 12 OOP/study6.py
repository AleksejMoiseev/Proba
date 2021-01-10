"""
Полиморфизм - подкласс изменяет поведение своего супер класса
оверайд берм метод из супер класса и переопределяем метод в детском классе
"""

# t = 'abba'
# t1 = t[::-1]
# print(t1)
# if t.lower() == t1.lower():
#     print("Зашибись")
# else:
#     print("не зашибись")
# def


class HomeAnimal:

    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def sound(self):
        pass

    @staticmethod
    def show(self):
        print(f"Имя животного{HomeAnimal.name}")
        return HomeAnimal.name


class Cat(HomeAnimal):
    def __init__(self):
        super().__init__(HomeAnimal.name, HomeAnimal._color)


"""
Практика
"""


class Person:

    Counter = 0

    def __init__(self, name, last_name, birth_year):
        self._name = name
        self._last_name = last_name
        self._birth_year = birth_year
        Person.Counter +=1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, val):
        self._last_name = val

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, val):
        self._birth_year = val

    @classmethod
    def get_number_of_instance(cls):
        return cls.Counter

    @staticmethod
    def get_number2_of_instance():
        return Person.Counter


class Calc:

    @staticmethod
    def max(k, l, m, n):
        return max(k, l, m, n)

    @staticmethod
    def min(k, l, m, n):
        return min(k, l, m, n)

    @staticmethod
    def factorial(n):
        fac = 1
        for i in range(2, n+1):
            fac *= i
        return fac

# def f(*arg):
# ...     print(arg)
# ...     print(type(arg))
# ...
# f(3,4,5,6)
# (3, 4, 5, 6)
# <class 'tuple'>


def boo(*args, **kwargs):
    print(*args)
    print(type(kwargs))
    print(kwargs)


def foo(*args, **kwargs):  # Принимает любое количество позишин  аргументов *args, принимает любое количество **kwargs кивордс  аргументов
    print(args)
    print(type(args))
    boo(*args, **kwargs)  # распаковывает список аргуметор при вызове функции звездочка работает на любой итерабле


if __name__ == '__main__':
    person = Person(name="Bob", last_name="banch", birth_year=2002)
    person1 = Person(name="Bob", last_name="banch", birth_year=2002)
    print(person.get_number_of_instance())
    print(Calc.factorial(5))
    foo(1, 2, 6, x=1)
