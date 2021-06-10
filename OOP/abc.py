class Abc:
    def __init__(self):
        self.my_my_list = [1, 2, 3]

    def __abs__(self):
        return [x**x for x in self.my_my_list]  # Посути сюда можем вернуть любой результат

if __name__ == '__main__':
    a = Abc()
    print(abs(a))  # результат возврата функции
