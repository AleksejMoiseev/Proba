#!/usr/bin/env python3
"""
Binary Search
Имплементировать функцию которая ищет целое число в сортированном
списке целых (binary_search(list_of_ints, num_to_search)). Если число
найдено вернуть индекс в списке, если не найдено -1. Использовать
алгоритм бинарного поиска. Если список не отсортирован выдать Exception
(реализовать проверку отсортированности в отдельной функции). Написать
тесты: позитивный и 2 негативных ( несортированный список, число
которое ищем не найдено)
"""
import math


def binary_search(list_of_ints, num_to_search):
    assert sort_check(list_of_ints), "Внимание , бинарный поиск работает " \
                                     "только с отсортированным LIST"
    counter = 0
    amount_of_elements = len(list_of_ints)
    low = list_of_ints[0]
    high = amount_of_elements
    if num_to_search == low:
        return 0
    while counter < math.log2(amount_of_elements):
        mid_index = round((high + low) / 2)
        if num_to_search == list_of_ints[mid_index]:
            return mid_index
        elif num_to_search < list_of_ints[mid_index]:
            high = mid_index
        else:
            low = mid_index
        counter = counter + 1
    return -1


def sort_check(list_of_ints):
    list_of_ints_sort = sorted(list_of_ints)
    for element in range(len(list_of_ints_sort)):
        if list_of_ints_sort[element] != list_of_ints[element]:
            return False
    return True


def positive_binary_search():
    assert binary_search([0, 2, 6, 9, 25, 50, 55, 111], 55) == 6


def negative_binary_search_no_sort():
    list_of_ints = [0, 2, 60, 9, 25, 50, 55, 111]
    assert sort_check(list_of_ints) == False, "Внимание проблемы с сортированными массивами"


def negative_binary_search_no_element():
    assert binary_search([0, 2, 6, 9, 25, 50, 55, 111], 150) == -1, "не работает с элементами отсутствующими в list"


if __name__ == '__main__':
    positive_binary_search()
    negative_binary_search_no_element()
    negative_binary_search_no_sort()
    print(binary_search([0, 20, 6, 9, 25, 50, 55, 111], num_to_search=6))
