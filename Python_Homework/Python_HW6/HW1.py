#!/usr/bin/env python3
"""
Пользователь с клавиатуры вносит названия файлов
пока не введет слово quit, после чего програма создает
новый файл содержащий содержимое всех файлов
В программе создано два файла для ввода:
1.txt
2.txt
значение обоих файлов записывается в третий файл результирующий:
3.txt
"""


# Функция для чтения файлов
def file_read(file_name):
    with open(file_name, "r+") as file:
        file_text = file.read()
    return file_text


flag = True
result_text = ""
while flag:
    try:
        file = input("Введите имя файла в формате имя.txt >>>")
        if file == "quit":
            raise Exception("Ввод данных закончен")
    except Exception:
        flag = False
    else:
        result_text = result_text + file_read(file) + " "

print(result_text)
with open("3.txt","wt") as file_result:
    file_result.write(result_text)