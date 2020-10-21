# Функция map это получает функция и лист и выдает новый лист
# формат map(func(), list)
names = ["€bentsi", "$Fedor", "€Ilya", "$Roman"]
new_names = []
for name in names:
    currency_suffix = "$" * len(name)
    name = currency_suffix + name
    new_names.append(name)
print(new_names)
print(list(map(str.upper, "bentsi")))
print((lambda x: x + 1)(3)) # формат написания lambda функции
obj = lambda x: x * 2
print(obj(2))

