#!/usr/bin/env python3
"""
проверяет является ли число палиндромом
"""


def reverse_line(sentence):
    value = str(sentence)
    list_value = list(value)
    list_value.reverse()
    value_reverse = "".join(list_value)
    return value_reverse


def palindrome_definition(sentence):
    value = str(sentence)
    middle = int(len(value)/2)
    if len(value) % 2 != 0:
        return False
    left_value = value[:middle]
    right_value = value[middle:]
    if left_value != reverse_line(right_value):
        return False
    return True


def test_palindrome_positive():
    result = palindrome_definition(546645)
    assert result == True


def test_palindrome_negative():
    result = palindrome_definition(421987)
    assert result == False


if __name__ == "__main__":
    test_palindrome_negative()
    test_palindrome_positive()
    print(palindrome_definition(123321))
