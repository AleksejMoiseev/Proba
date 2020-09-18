num1 = int(input("Enter number 1 > "))
num2 = int(input("Enter number 2 > "))
num3 = int(input("Enter number 3 > "))
flag = True
print("Для нахождения max из чисел выберите 'a' ")
print("Для нахождения min из чисел выберите 'b' ")
print("Для нахождения среднего значения  из чисел выберите 'c' ")
while flag:
    menu_selection = input("Сделайте выбор > ")
    if menu_selection == 'a' or\
       menu_selection == 'b' or\
       menu_selection == 'c':
        flag = False
if menu_selection == 'a':
    max_value = max(num1, num2, num3)
    print(f"Максимальное из трех чисел> {max_value}")
elif menu_selection == 'b':
    min_value = min(num1, num2, num3)
    print(f"Минимальное из трех чисел> {min_value}")
else:
    print(f"Среднее значение> { (num1 + num2 + num3) / 3 }")