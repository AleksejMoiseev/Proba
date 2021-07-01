
class DescriptorValue:
    def __set_name__(self, owner, name):
        self.__name = name

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point:
    X = DescriptorValue()
    Y = DescriptorValue()
    Z = DescriptorValue()

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


if __name__ == '__main__':
    p = Point(1, 2, 3)
    p1 = Point(10, 20, 30)
    print(p.X, p.Y, p.Z)

