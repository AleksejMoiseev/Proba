print("Введите значения для получения фигуры: а, б, в, г, д")
choice = input("введите значение: > ")
assert 'а'<= choice <= 'д', "Введите значения для получения фигуры: а, б, в, г, д"
str= ""
const_n = 10

if choice == 'а':
    for i in range(const_n):
        print('')
        for j in range(const_n):
            if j <= i:
                print(" ", end="")
            else:
                print("*", end="")
elif choice == 'б':
    for i in range(const_n):
        print('')
        for j in range(10):
            if j > i:
                print(" ", end="")
            else:
                print("*", end="")
elif choice == 'в':
    for i in range(const_n, 0, -2):
        str = str + " "
        print(str + '*' * i)
elif choice == 'г':
    for i in range(1, const_n, 2):
        for j in range(0, int((const_n - i) / 2), 1):
            print(" ", end="")
        for j in range(0, i, 1):
            print("*", end="")
        print("")
else:
    for i in range(const_n, 2, -2):
        str = str + " "
        print(str + '*' * i)
    print(str + " " + '*' * 2, end="")
    str = str + " " * 3
    for i in range(0, const_n + 2, 2):
        str = str[:-1]
        print(str + '*' * i)