# Операторы in not in
list_pr = [1, 2, 3, 4, 5, 6, 7]
if 4 in list_pr:
    print("ok")
print(4 in list_pr)
print(4 not in list_pr)
# Найти самое большое значение в списке
value_max = list_pr[0]
for i, num in enumerate(list_pr):
    if num > value_max:
        value_max = num
        index_max = i
print(i, num)
# Нахождение индекса заданного числа
to_find = 5
for i, num in enumerate(list_pr):
    if num == to_find:
        break
print(f"index = {i}")
# Пайтоник
if to_find in list_pr:
    print("Она вертится")
