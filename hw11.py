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

    def get_info(self):
        print(f'This vehicle could reach {self.max_speed} km/h')

class Plane(Vehicle):
    max_speed = 800
    size = 'big'

    def get_info(self):
        print(f'This vehicle could reach {self.max_speed} km/h')

class Ship(Vehicle):
    max_speed = 60
    size = 'enormous'

    def get_info(self):
        print(f'This vehicle could reach {self.max_speed} km/h')

mersedes = Auto()
boieng = Plane()
MGS = Ship()

print(mersedes.get_info())
print(boieng.get_info())
print(MGS.get_info())