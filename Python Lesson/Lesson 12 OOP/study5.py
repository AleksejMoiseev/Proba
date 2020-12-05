"""
Класс композишн
"""


class Address:

    def __init__(self, street, city):
        self.street = street
        self.city = city


class Emloyee:

    def __init__(self, employee, name, address):
        self.employee = employee
        self.name = name
        self.address = address

    def city(self):
        return self.address.city  # Позволяет  дотягиваться до других обьектов класса, которые сами являются
                                  # переменными этого класса


my_adress = Address(street="Pionerskaya", city="Tula")
my_employee = Emloyee(1, "Алексей", my_adress)
print(my_employee.city())
