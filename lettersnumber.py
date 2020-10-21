"""
Пользователь вводит с клавиатуры строку. Посчитайте количество букв и цифр
выведите оба количества на экран
"""


def count_letters(some_str):
    counter = 0
    for char in some_str:
        if char.isalpha():
            counter += 1
    return counter


def count_numbers(some_str):
    counter = 0
    for char in some_str:
        if char.isdigit():
            counter += 1
    return counter


def get_string():
    return input("Enter a string of letters and numbers> ")


def main():
    some_string = get_string()
    amount_numbers = count_numbers(some_string)
    amount_letters = count_letters(some_string)
    print(f"Amount of numbers in {some_string} is {amount_numbers}")
    print(f"Amount of numbers in {some_string} is {amount_letters}")


if __name__ == "__main__":
    main()