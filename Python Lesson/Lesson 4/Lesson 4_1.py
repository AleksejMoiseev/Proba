# Списки Сохраняе в себе n обьектов, можно хранить разные типы
numbers = [10, 5, 7, 2, 1]
print(numbers)
# Печать нулевого элемента
print(numbers[0])
# Изменения элемента списка
numbers[1] = 84
print(numbers[1])
# размер списка длина
print(len(numbers))
# Печать последнего элемента пайтоник Отрицательные индексы
print(numbers[-1])
# Удаление элемента списка
del numbers[1]
print(numbers)
# Срезы
print(numbers[1:3])
# ФУНКЦИЯ List ПЕРЕСОЗДАЁТ СПИСКИ
numbers_COPY = list(numbers)
print(id(numbers))
print(id(numbers_COPY))
# Методы
# Прочитать все методы
# print(dir(numbers))
# вызов метода через " . "
# удаляет последний элемент и возвращает его
print(numbers.pop())
print(numbers)
# Добавляет в конец элемент
numbers.append(4)
# Переворачивает реверсом
numbers.reverse()
print(numbers)
# Считает количество вхождений в список
print(numbers.count(7))
print(numbers)
# Метод extend
numbers.extend([1, 2, 3])
print(numbers)
# Сортировка  списка
num = [423, 1340]
num.sort()
print(num)
# Поставить значение в ячейку
numbers.insert(2, 456)
print(numbers)
# list comprehension
names = ['bentsy', 'fedor']
names_honored = [name.capitalize() for name in names]
print(names_honored)