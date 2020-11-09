"""
ООП Вводное занятие
"""

# Создание класса
# Начинается с боьшой буквы и через камэл кейс


class PersonClass:
    name = ""
    designation = ""

    def learn(self):
        print(" Привет")

    def walk(self):
        print("Walk")

    def eat(self):
        print("{hev [hev")


class Singer(PersonClass):
    band_name = ""

    def play_guitar(self):
        print("Играю на гитаре")

    def sing(self):
        print("Kgf ЛА ЛПА")


if __name__ == '__main__':
    new_man = PersonClass()