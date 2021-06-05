'''
Описана возможность создания итератора методы __iter__ и __next__
Можно класс сделать итерэбэл и итерироваться по нему.
'''

class MyIter:

    def __init__(self, limit, name):
        self.limit = limit
        self.name = name
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.limit:
            raise StopIteration

        self.start += 1
        return self.start


if __name__ == '__main__':
    it = MyIter(limit=10, name='Alex')
    for i in it:
        print(i, f"{it.name}_{i}")



