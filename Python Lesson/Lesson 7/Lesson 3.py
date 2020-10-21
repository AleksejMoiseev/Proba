"""
Написать программу по определению счастливого билета
"""


def sum_digits(number_str):
    sum_of_digits = sum([int(i) for i in number_str])
    return sum_of_digits


def is_luck_number(num):
    number = str(num)
    if len(number) % 2 != 0:
        raise Exception(f"Sorry{num} is not Length")
    mid = len(number)//2
    left = number[:mid]
    right = number[mid:]
    return sum_digits(left) == sum_digits(right)


def test_is_lucky_number_exception():
    try:
        is_luck_number("12345")
    except Exception:
        return True
    else:
        raise Exception("Test failed: exception but didnt get one")


if __name__ == "__main__":
    assert is_luck_number(num=123420) == True
    assert is_luck_number(num=723422) == False
    test_is_lucky_number_exception()