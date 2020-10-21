"""
Работа с файлами чтение и запись
"""


def file_read():
    file1 = open("/home/alameda/Документы/1.txt", mode="r")  # Открытие файла для записи
    file1_rtad = file1.read()  # Чтение файла
    file1.close()  # закрытие файла
    print(file1_rtad)


def file_write(name):
    file1 = open("/home/alameda/Документы/1.txt", mode="a")  # Открытие файла с модом для записи"a"
    file1_rtad = file1.write(name)  # Запись файла
    file1.close()  # закрытие файла


if __name__ == '__main__':
    file_write("Andrej")  # записали в файл
    file_read()  # прочитали  в файл