"""
__setattr__(self, key, value):  # Автоматически вызывается при при изменении свойства  key класса
"""


class CheckSetattr:

    def __init__(self, name):
        print('Отработал метод init')
        self.name = name

    def __setattr__(self, key, value):  # Автоматически вызывается при при изменении свойства  key класса
        print('Отработал метод __setattr__')
        self.__dict__[key] = value

    def __getattr__(self, item):  # Вызывается при попытке получить не существующее свойство
        print('getattr_')
        return 'Хреново'

    def __getattribute__(self, item):  # вызывается всегда независимо не отчего при получении свойства обтекта,
        # любое обращение к обьекту
        print('Отработал метод __getattribute__')
        return object.__getattribute__(self, item)


if __name__ == '__main__':
    ins = CheckSetattr(name='Alex')
    print(ins.__getattribute__(item='name'))
    ins.name = 'Fedor'
    print(ins.name)
    print(ins.last_name)
