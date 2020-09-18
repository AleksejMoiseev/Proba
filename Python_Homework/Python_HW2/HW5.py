start_value = int(input("Enter start value> "))
end_value = int(input("Enter finish value> "))
start = start_value
end = end_value
counter = 0
if end_value < start_value:
    start = end_value
    end = start_value
print("а. Все числа диапазона")
for i in range(start, end + 1, 1):
    print(i)
print("b.Все числа в убывающем порядке")
for i in range(end, start - 1, -1):
    print(i)
print("c.Все числа кратные '7' ")
for i in range(start, end + 1, 1):
    if i % 5 == 0:
        counter = counter + 1
    if i % 7 == 0:
        print(i)
print(f"d.Количество чисел кратных '5' равно: {counter}")