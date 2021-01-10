import ast
"""
Почитать про  eval and literal_eval, функцию repr, модуль ast
"""
# имеем словарь
data = {"type": "A", "field": "value1", "field1": "value2"}
# запишем  через функцию repr в текстовый файл
with open("newfile.txt", "wt") as file:
    file.write(repr(data))
"""
функция repr позволяет превратить обьект в строку и записать 
его в текстовый файл
для восстановления обьекта применяется функция literal_eval
и это работает если структура данных имеет не сложную структуру
"""
with open("newfile.txt", "rt") as file:
    text = file.read()
    obj = ast.literal_eval(text)
print(type(obj))  # Обьект восстановлен
