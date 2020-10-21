import random
# Рандомное число
print((random.random() * 10))
# Рандомное число от 0 до 10
print(random.randint(0, 10))
# Выбирает из листа списка любое число
names = ["bentsi", "Akeksej"]
print(random.choice(names))
# Samples выбирают несколько уникальных элементовб получаем список
print(random.sample(names, 2))