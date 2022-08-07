"""
Створіть клас "Транспортний засіб" та підкласи "Автомобіль",
 "Літак", "Корабель", наслідувані від "Транспортний засіб".
  Наповніть класи атрибутами на свій розсуд.
 Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

"""


class Vehicle:
    numeber_of_vehicles = None


class Auto(Vehicle):
    max_speed = 120
    size = 'small'


class Plane(Vehicle):
    max_speed = 800
    size = 'big'


class Ship(Vehicle):
    max_speed = 60
    size = 'enormous'


mersedes = Auto()
boieng = Plane()
MGS = Ship()
