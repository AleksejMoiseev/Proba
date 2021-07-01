"""

Создание класса  Singelton
"""

class SingeltonClass:

    __instance = None


    def __init__(self, name, last_name):
        print('вызван констрактор init')
        self.name = name
        self.last = last_name


    def __new__(cls, *args, **kwargs):
        print('Вызван метод NEW')
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance



if __name__ == '__main__':
    s = SingeltonClass(name='Alex', last_name='Moiseev')
    s1 = SingeltonClass(name='Masha', last_name='frolova')
    print(id(s.name), id(s1.name))