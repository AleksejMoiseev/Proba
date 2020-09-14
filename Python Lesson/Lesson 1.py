value = int(input("Enter first value> "))
percent = int(input("Enter percent > "))
# Возможная запись в принт
print("Your value", value * percent / 100)
# Новая запись синтаксический сахар записи в функции принт
print(f"Your value{value * percent / 100}")
# Старая запись
print("%s%% from %s = %s" % (value, percent, value * percent / 100))