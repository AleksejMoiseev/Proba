# оператор сравнения равенства ==
from datetime import  datetime
t1 = datetime.now()
t2 = datetime.now()
# можем сравнивать обьекты <=.>=,==
print(t1 < t2)
# формат написания условия
if t2 < t1:
    print("привет")
elif t1 == t2:
    print("Снова привет")
else:
    print("не привет")
# не больше двух вложеных if
