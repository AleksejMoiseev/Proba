# Strings
hello = "Hello world"
# Определение длины строки
print(len(hello))
# Печать строки более чем 79 символов перенос строки
message = """Hello
world"""
message = "--------------  Печать строки более чем 79" \
          "символов перенос строки  ----------------"
print(message)
multi_line = """
   Line 1
Line 2
"""
print((multi_line))
# Modul textwrab убирает табуляцию впереди строк
# from textwrap import dedent если нужен один модуль
# import textwrap если нужны все модули textwrap
from textwrap import dedent

multi_line = dedent("""
  Line 1
  Line 2
""")
print(multi_line)
# List от стринга получаем список отдельных символов
list1 = list(hello)
print(list1)
# выводит индекс с которого начинается "l'
print(hello.index('l'))
# Метод count считает сколько значений буквы в слове
print(hello.count("l"))
# окружает строку символами по образцу ниже
print(hello.center(20, "$"))
# Метод find выводит индекс элемента, если не находит возвращает -1
print(hello.find("g"))  # вернет -1 потому что 'g' нет в переменной hello
# Метод isspase() возвращает тру если это пробел
print(" ".isspace())
# Метод strip убирает лишние пробелы и слеши а также можно удалять последние символы
hello.strip()  # Удалит последний символ d
print(hello)
# Метод join()
print("$".join(list1))  # Обьединяет символы вокруг заданого Символа
# Метод split разбиваем получаем список каждый элемент список представляет отдельный элемент
list2 = hello.split(" ")
print(list2)
# Метод replace меняет одно значение на другое и возвращает новую строку
print(hello.replace("Hello", "world", 1))  # Меняем только одно значение можно поменять больше


# Метод Title() каждое новое слово с большой буквы
# Функции
def power(number, exp):
    print(number ** exp)
    return number ** exp


power(number=10, exp=2)
# Анонимная функция используется один раз и потом умирает

print(sorted(list2, key=lambda list_obj: list_obj[0]))