#!/usr/bin/env python3
"""
1 написать generator функцию cycle которая будет получать iterable и
возвращать элементы iterable по кругу бесконечно.
2 Написать функцию iter_n_times(iterable, n) которая будет получать iterable и
возвращать iterable с n повторениями.
"""
from time import sleep


def generator_for_cycle(arr):
    while True:
        for i in arr:
            yield i


def cycle(arr):
    generator = generator_for_cycle(arr=arr)
    for value_in_generator in generator:
        sleep(1)
        print(value_in_generator)


def iter_n_times(arr, number_of_repeat):
    return arr * number_of_repeat


print(iter_n_times(arr="abc", number_of_repeat=2))
if __name__ == "__main__":
    cycle(arr=[1, 2, 3])
