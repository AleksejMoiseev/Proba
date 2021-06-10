class Len:
    def __init__(self):
        self.my_my_list = [1, 2, 3]

    def __len__(self):  #  Позволяет возвращать длину переменой которая будет означать длину класса
        return len(self.my_my_list)


if __name__ == '__main__':
    l = Len()
    print(len(l)) # Возвращаем длину класса Len
    print('Что это ', l.__sizeof__())  # показывает количество байт для обслуживания этого класса
    print(l.__dict__.__sizeof__())  # размер памяти для обслуживания dict коллекции

    