"""
Tuple - кортеж, immutable  не изменяемы const
"""
thistuple = ("apple", "banana", "cherry")# создание через круглые скобки
new_tuple = tuple("Bentsy") # создание через функцию tuple
print(new_tuple)  # ('B', 'e', 'n', 't', 's', 'y') результат
print(new_tuple[:3])  # ('B', 'e', 'n') результат
print(id(thistuple))   # tuple не создает новый tuple
# Set - множество
thisset = {"apple", "banana", "cherry"}  # определяется через скобки {}
thisset.add("orange") # добавляет в set orange
thisset.update(["orange", "mango"])  # добавляет несколько элементов из  list
# set содержит только уникальные элементы
my_set = {"apple", "banana", "banana"}
print(my_set)  # {'apple', 'banana'} результат
print(thisset)
# алгебра множеств преминима к set
# обьединение union
new_set = thisset.union(my_set)
print(new_set)  # 'apple', 'banana', 'orange', 'cherry', 'mango'} обьединяет два множества
# пересечение
new_set2 = thisset.intersection(my_set) # Включает только общие элементы
print(new_set2)  # {'apple', 'banana'}
# разность - убрать элементы одного множества из другого
new_set3 = thisset.difference(my_set, {"cherry"}) # вычитает my_set + cherry
print(new_set3)  # {'mango', 'cherry', 'orange'} результат
# symmetric-diffence
new_set4 = thisset.symmetric_difference(my_set)
print(new_set4)
# переделка list в set
# new4 = {[1, 2, 3]}
# print(new4)  # {1, 2, 3} результат переделки list
# Словари dictionary
# состоит из ключей и значений, ключи уникальны на каждый ключ одно значение это любой обьект
# определени
car = {
    "brand": "Ford",
    "model": "Mustang",
    "years": 2008
}
print(car.keys())  # Печатает все ключи
print(car.values())  # Печатает все значения
print(car["brand"])  # печатает значения ключа "brand"
from pprint import pprint # импорт  pprint
pprint(car, width=10)
# Если ключ не существует программа посыпится
# можно обращаться через get
print(car.get("ret", "Defolt Сюда пишем пояснения"))  # если такого ключа нет вернется None
print(car.get("brand", "Defolt Сюда пишем пояснения"))  # возвращает значения
print(len(car))  # количество ключей
car["brand"] = "BMW"  # Изменили значение
print(car["brand"])
print(car.pop("brand"))  # Удаление значения с ключом
print(car.items())  # показывают ключ и значение вернул лист
for k, v in car.items():
    print(f"k = {k}, v = {v}")
# добавление ключа в значение можно записать любой вид данных в том числе и лист
car["brand"] = "bmw"
pprint(car, width=10)
car["chidren"] = {"child": "emil", "years": 2001}
pprint(car, width=10)
# Метод set добавляет элементы с проверкой по ключу
# Метод update ОБНОВЛЯЕТ СЛОВАРЬ ДОБАВЛЯЯ ЗНАЧЕНИЯ КОТОРЫХ НЕ БЫЛО




