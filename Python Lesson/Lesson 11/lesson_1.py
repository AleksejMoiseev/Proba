"""
Работа с файлами
"""

# открытие файла  если файла не существует

try: # изучить  по видео о исключениях
    open("not_found.txt")
except FileNotFoundError as ex:
    print(ex)

from pathlib import Path #  можно делать обьект "путь"
p = Path("/home/")
str = p.open()  # Открывает файл
str.write()  # записывает в файл
str.flush()  # Выгрузить в файл
str.close()  #  закрытие файла


# Альтернативное решение
with open(file="data.text", mode="w") as file:
    file.writelines(["Romh", "Ilya"])          # контекст менеджер


