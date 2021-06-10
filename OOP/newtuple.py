from collections import namedtuple

Car = namedtuple('Car', ['color', 'pay'])

my_car = Car(color='red', pay=50)
print(my_car.pay, my_car.color)
print(Car.__name__)


