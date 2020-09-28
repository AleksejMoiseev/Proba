import random
list_one = []
list_two = []
const_n = 10
for i in range(const_n):
    value_temp = random.randint(0, 50)
    value_temp1 = round(random.random() * 10)
    list_one.append(value_temp1)
    list_two.append(value_temp)

list_result_a = list_one[:]
for i in list_two:
    list_result_a.append(i)

list_result_b = []
list_result_c = []
list_result_d = []
for value in list_result_a:
    if value not in list_result_b:
        list_result_b.append(value)
    if (value in list_one) and (value in list_two):
        list_result_c.append(value)
    if not((value in list_one) and (value in list_two)):
        list_result_d.append(value)

list_result_e = []
list_result_e.append(min(list_one))
list_result_e.append(max(list_one))
list_result_e.append(min(list_two))
list_result_e.append(max(list_two))

print("Список содерщащий элементы обоих списков")
print(list_result_a)
print("Список содержащий элементы списка без повторений")
print(list_result_b)
print("Общие элементы для обоих списков")
print(list_result_c)
print("Уникальные элементы списков")
print(list_result_d)
print("Экстремум списков")
print(list_result_e)

