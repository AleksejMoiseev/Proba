"""
Ternary if
"""
number = int(input("Enter int number"))
if number % 2 == 0:
    message = "even"
else:
    message = "od"

print(f"value = {message}")

# можно заменить на тернари if
message = "even" if number % 2 == 0 else "od"
