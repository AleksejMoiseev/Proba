# Циклы
# от старт = 3 до 10 с шагом 2
for i in range(3, 10,  2):
    print(i)
# Continue пропускает иттерацию
# break прекращает цикл
for i in range(84):
    if i == 10:
        continue
    if i == 84:
        break
    print(i)
# float("-inf") минус бесконечность
# print(max(1, 2, 3)) ищет максимальное число
print(max(1, 2, 3))
begin_range = int(input("Enter start of the range> "))
end_range = int(input("Enter end of the range> "))
for i in range(begin_range, end_range + 1, 1):
    print(i)
# Цикл While
x = 10
while x > 0:
    x = x - 1
    print(x)

