import math
# Ошибки обход
x = int(input(">"))
y = 0
try:
    y = math.sqrt(x)
except ValueError:
    print("Отрицательное число")
print(y)
# Создание exception
if y == 0:
    raise Exception("Черт возьми это деление на ноль")