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

    def __getitem__(self, item):  # При переопределении метода позволяет обращаться к атрибутам как к словарю
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == 'name':
            return self.name
        return None

    def __setitem__(self, key, value):  # Позволяет работать с обьектом как со словарем
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, str):  # прописываем ограничения на параметры key, value
            raise ValueError("значение должен быть строкой")
        if key == 'name':
            self.name = value


if __name__ == '__main__':
    ins = CheckSetattr(name='Alex')
    print(ins.__getattribute__(item='name'))  #Получаем обьект через метод __getattribute__
    ins.name = 'Fedor'  # вызываем метод __setattr__, __getattribute__
    print(ins.name)  # Вызываем метод __getattribute__
    print(ins.last_name)  # вызываем метод __getattr__
    print(ins['name'])  # Обращаемся к свойству класса как словарю благодаря переопределению метода  __getitem__
    ins['name'] = 'Alex'
    print(ins.name)

