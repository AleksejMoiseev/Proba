import json

"""
Работа с @property  получение геттера  и сеттера через декоратор
"""


class Person:
    def __init__(self, name, *args):
        self.name = name

    @property
    def name(self):  # Геттер
        return self.__name

    @name.setter  # Сеттер
    def name(self, value):
        self.__name = value

    def __str__(self):
        return "Person:{}".format(self.name)

    def __to_json(self):
        return {'name': self.name}

    def to_json(self):
        return json.dumps(self.__to_json())

    @staticmethod
    def from_json(js):
        return json.loads(js)

    def pprint(self):
        print("вызов метода person")

    def __getitem__(self, item):  # Позволяет оргазовать обращение к свойствам класса как Instance_Class['name']
        print("Отработал метод __getitem__")
        if item == 'name':
            return self.name

    def __setitem__(self, key, value):  # Перегрузка метода для обращению к свойствам как к словарю
        print('Отработал метод __setitem__ ')
        if key == "name":
            self.name = value


class CheckSettator:

    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        print("key", key)
        print(('value', value))
        self.__dict__[key] = value

    def __getattr__(self, item):
        print('getattr_')

    def __getattribute__(self, item):
        print('Отработал метод __getattribute__')
        return object.__getattribute__(self,item)

if __name__ == '__main__':
    p = Person('Alex')
    print(p.name)
    p.name = "Dima perdun"
    print(p.name)
    print(getattr(p, 'name', False))  # Функция getattr дает атрибут обьекта
    print(p.__dict__)
    d = {'name': 'Alex'}
    p1 = Person(**d)
    print(p1)
    js = json.dumps(d)
    print(js)
    d1 = json.loads(js)
    print(d1)
    print(p.to_json())
    print(p1.to_json())
    js1 = p1.to_json()
    print(p.from_json(js1))
    person = p.from_json(js1)
    print(Person(**person))
    check = CheckSettator(name='AAlex')
    check.booo  # Вызывается метод def __getattr__(self, item):
    print('Отработал метод ef __getitem__ ', p['name'])
    p['name'] = 'Aleksej'
    print('Отработал метод ef __getitem__ ', p['name'])