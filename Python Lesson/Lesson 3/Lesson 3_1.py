hour = int(input("Enter time> "))
# Проверка на ошибку
assert 0 <= hour <= 23, "Hour must be between 0 and 23"
if 0 <= hour < 6:
    print("Good night!")
elif 6 <= hour < 13:
    print("Good morning")
elif 13 <= hour < 17:
    print("Good day")
else:
    print("Good evening")

