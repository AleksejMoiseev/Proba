import datetime  # Импортируем модуль datetime
import time  # Импортируем модуль time
# Присваиваем  i значение сегодняшней даты
i = datetime.date.today()
# Присваиваем h  значение текущего времени
h = datetime.datetime.today().strftime("%M:%S")
print(h)