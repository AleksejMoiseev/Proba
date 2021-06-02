from OOP.property_OOP import Person


class Individual(Person):

    def __init__(self, last_name, name):
        self.last_name = last_name
        Person.__init__(self, name)

class People:
    def __init__(self, student:Individual, description:str, discharge:int):  # Двоеточие означает, это анотация
        self.student = student
        self.description = description






if __name__ == '__main__':
    i = Individual(name='Alex', last_name='Moiseev')
    p = People(student=i, description="Это студент", discharge=3)