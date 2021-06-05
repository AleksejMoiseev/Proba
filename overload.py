"""
Демонстрация работы функции  super() и overload method
"""

from OOP.property_OOP import Person


class Individual(Person):

    def __init__(self, last_name, name):
        super().__init__(name=name)  # образец работы с методом super при инициализации вместе с переменными Base класса
        self.last_name = last_name

    def __str__(self):
        return f"Student {self.name} {self.last_name}"

    def pprint(self):
        super().pprint()  # Обращение к функции base класса  через функцию super
        print("вызываю метод в класе Individual")
        return "вызываю метод в класе Individual"


class People:
    def __init__(self, student: Individual, description: str, discharge: int):  # Двоеточие означает, это анотация
        self.student = student
        self.description = description
        self.discharge = discharge


if __name__ == '__main__':
    i = Individual(name='Alex', last_name='Moiseev')
    p = People(student=i, description="Это студент", discharge=3)
    print(p.student)
    print(p.student.to_json())
    print(p.student.pprint())
