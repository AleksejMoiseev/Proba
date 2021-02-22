"""
 В Python  можно создать свой contex manager
 при создании класса  CM необходимо дополнительно
 определить 2 метода
 __enter__  and __exit__
"""
from contextlib import contextmanager


class ContexManager:
    def __init__(self):
        print("Init mrthod")

    def __enter__(self):
        print("enter method ")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method")


@contextmanager
def contex_example():
    print("init")
    yield
    print("on exit")




if __name__ == '__main__':
    with ContexManager() as cm:  # запускается init  далее __enter__
        print("insid contex")  # запускается тело
    print("Finito")  # запускается  __exit__
