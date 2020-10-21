start_value = int(input("Enter start value> "))
end_value = int(input("Enter finish value> "))
assert start_value != end_value, "Введите отличные друг от друга значения"
start = start_value
end = end_value
if end_value < start_value:
    start = end_value
    end = start_value

counter_even = 0
counter_odd = 0
sum_even = 0
sum_odd = 0
for i in range(start, end + 1, 1):
    if i % 2 == 0:
        sum_even = sum_even + i
        counter_even = counter_even + 1
    if i % 2 != 0:
        sum_odd = sum_odd + i
        counter_odd = counter_odd + 1
print(f"Количество четных чисел: {counter_even}")
print(f"Среднеарифметическое: {sum_even/counter_even}")
print(f"Количество не четных чисел: {counter_odd}")
print(f"Среднеарифметическое: {sum_odd/counter_odd}")
