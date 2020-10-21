"""
Напишите функцию которая проверяет простое ли число
если функция возвращает bool в названии ставим is
"""


def is_prime(number):
    if number == 1 or number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    assert is_prime(7) == True
    assert is_prime(10) == False