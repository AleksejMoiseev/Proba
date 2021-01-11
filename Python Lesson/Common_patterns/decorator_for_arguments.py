"""
Декоратор с аргументами
"""
import time
import random
from functools import wraps


def timing(debug_mode=True):
    def _timing(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            if debug_mode:
                print("Start time:", start_time)
            return_val = func(*args, **kwargs)
            end_time = time.time()
            if debug_mode:
                print("End time:", end_time)
            return return_val
        return inner
    return _timing


@timing(debug_mode=False)
def foo(start, stop):
    """Привет"""
    print("starting to run.....")
    time.sleep(random.randint(start, stop))
    print("Stopped runing....")


if __name__ == '__main__':
    foo(start=1, stop=5)
    print(foo.__doc__)