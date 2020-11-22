"""
Написать класс Person
"""


class Person:
    name = ""
    designation = ""

    def lern(self):
        print("Учусь")

    def walk(self):
        print("Гуляю")

    def eat(self):
        print("EM")


class Programmer(Person):
    company_name = ""

    def coding(self):
        print("Пишу программу")


class Dancer(Person):
    group_name =""

    def dancing(self):
        print("Танцует")


class Singer(Person):
    band_name = ""

    def sunging(self):
        print("Пою песни")

    def play_gitar(self):
        print("Играю на гитаре")


def main():
    vova_programmer = Programmer()
    vova_programmer.name = "Vova"
    vova_programmer.designation = "Вован"
    print(vova_programmer.designation)
    vova_programmer.coding()
    vova_programmer.eat()
    vova_programmer.walk()
    print()
    masha_dancer = Dancer()
    masha_dancer.name = "Маня"
    masha_dancer.designation = "Облигация"
    print(f"Великая {masha_dancer.name} по кличке {masha_dancer.designation}")
    masha_dancer.dancing()


if __name__ == '__main__':
    main()
