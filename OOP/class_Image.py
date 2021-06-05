"""
10: собственные исключения и итерабельные объекты, методы __iter__ и __next__
Пример использование методов __setitem__, __getitem__
"""


class ImageXIterator:

    def __init__(self, image: object, y: int):
        self.limit = image.width
        self.x = 0
        self.image = image
        self.y = y

    def __iter__(self):
        return self

    def __next__(self):
        if self.x >= self.limit:
            raise  StopIteration

        self.x += 1
        return self.image[(self.x-1, self.y)]


class ImageYIterator:

    def __init__(self, image: object):
        self.limit = image.height
        self.y = 0
        self.image = image

    def __iter__(self):
        return self

    def __next__(self):
        if self.y >= self.limit:
            raise StopIteration
        self.y += 1
        return ImageXIterator(self.image, self.y - 1 )




class Image:

    def __init__(self, width: int, height: int, background='_'):
        self.__width = width
        self.__height = height
        self.__background = background
        self.__colors: set = {self.__background, }
        self.__pixels: dict = {}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("Сюда пишем значение в PX  в  виде строки")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Сюда пишем значение в PX  в  виде строки")
        self.__height = value

    def __setitem__(self, coordinate, color):

        if color == self.__background:
            self.__pixels.pop(coordinate, None)
        else:
            self.__pixels[coordinate] = color
            self.__colors.add(color)

    def __getitem__(self, coordinate):
        return self.__pixels.get(coordinate, self.__background)

    def __iter__(self):
        return ImageYIterator(image=self)




if __name__ == '__main__':
    img = Image(20, 4)
    print(img.height, img.width)
    img[(1, 1)] = 'red'
    print(img[(1, 1)])
    for y in range(img.height):
        for x in range(img.width):
            print(img[x, y], sep=' ', end='')
        print()

    for row in img:
        for pixel in row:
            print(pixel, sep=' ', end='')
        print()


