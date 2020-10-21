"""
filter, Zip
"""
from random import randint
# функция фильт сортирует элементы по определенному фильтру определенной функцией
e = [1, 2, 3, 4]
f = filter(lambda x: x > 2, e)  # Это генератор
print(f)
data = [randint(-10, 10) for _ in range(10)]  # _ ПРИМЕНЯЕТСЯ ЕСЛИ переменная более нигде не используется
print(list(f))  # результат [3, 4]
# вместо ламбды можем писать



def positive_even(x):
    if x > 0 and x % 2 ==0:
        return True
    return False


f1 = filter(positive_even, data)  # используем свою функцию
print(list(f1))

# Zip
names = ["Bentsi", "Alexey", "Julia", "Fedor"]
salaries = [100, 200, 300, 400]
# name_salary -> [("Bentsi", 100), ("Alexey", 200), ...] # результат
name_salary = list(zip(names, salaries))
print(name_salary)
print(dict(name_salary))

