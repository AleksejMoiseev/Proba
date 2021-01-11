"""
Прочитать про ISBN
Читаем про декораторы
"""
import copy
from functools import wraps

copy.copy(x='')  # Shallow Copy  создает копию  которые омеют одинаковые обьекты
copy.deepcopy(x='')  # deep copy Создаем полную копию обьектов которые имеет все разные референсы на все обьекты

"""
Декоратор способ изменить поведения функции или метода 
например @timeit - перед запуском функции когда функция начала работать, сколько бежала, и когда закончила
"""
import time
import random


def timing(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        print("Start time:", start_time)
        return_val = func(*args, **kwargs)
        end_time = time.time()
        print("End time:", end_time)

    return inner


@timing
def foo(start, stop):
    """Привет"""
    print("starting to run.....")
    time.sleep(random.randint(start, stop))
    print("Stopped runing....")


if __name__ == '__main__':
    foo(start=1, stop=5)
    print(foo.__doc__)