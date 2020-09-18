num = int(input("Введите число в диапазоне от 1 до 100> "))
assert 1 <= num <= 100, "value mast be between 1 and 100"
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif not (num % 3 == 0 and num % 5 == 0):
    print(num)