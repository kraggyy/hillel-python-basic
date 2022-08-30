class IsInteger:

    @classmethod
    def verify_item(cls, item):
        if type(item) != int:
            raise TypeError('value must be int')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class IsString:

    @classmethod
    def verify_item(cls, item):
        if type(item) != str:
            raise TypeError('value must be str')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class IsFloat:

    @classmethod
    def verify_item(cls, item):
        if type(item) != float:
            raise TypeError('value must be float')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class Vehicle:
    producer = IsString()
    model = IsString()
    year = IsInteger()
    tank_capacity = IsFloat()
    tank_level = IsFloat()
    max_speed = IsInteger()
    fuel_consumption = IsFloat()
    odometer_value = IsInteger()

    def __init__(self, producer, model, year, tank_capacity, max_speed, fuel_consumption):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = float(0)
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = int(0)

    def __repr__(self):
        return f'Произведена в {self.year}, марка {self.producer}, маодель {self.model}, ' \
               f'одометр {self.odometer_value}'

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            raise TypeError('wrong argument')
        conditions = [
            self.year == other.year,
            self.odometer_value == other.odometer_value
        ]
        return all(conditions)

    @property
    def max_distance(self) -> int:
        return int(self.tank_level * 100 / self.fuel_consumption)

    def refueling(self):

        tank_refueling = self.tank_capacity - self.tank_level
        self.tank_level = self.tank_capacity
        print(f'Заправили на {tank_refueling} литров')

    def race(self, distance):

        if not isinstance(distance, int):
            raise TypeError('value must be int')
        rase_distance = distance if self.max_distance > distance else self.max_distance
        total_fuel_consumption = (rase_distance * self.fuel_consumption) / 100
        self.tank_level -= total_fuel_consumption
        self.odometer_value += rase_distance
        res = {
            'дистанция': rase_distance,
            'в баке': self.tank_level,
            'время гонки': rase_distance / (self.max_speed * 0.8)
        }
        return res

    def lend_fuel(self, other):

        if not isinstance(other, Vehicle):
            raise TypeError('wrong argument')
        need_fuel = self.tank_capacity - self.tank_level
        available_fuel = other.tank_level
        if need_fuel == 0:
            print('Уже полный бак')
        elif available_fuel == 0:
            print('Нет бензина')
        else:
            tank_refueling = need_fuel if need_fuel < available_fuel else available_fuel
            self.tank_level += tank_refueling
            other.tank_level -= tank_refueling
            print(f'Перелили {tank_refueling} литров бензина')


if __name__ == '__main__':
    car1 = Vehicle(
        producer='Mercedes',
        model='CLS AMG',
        year=2000,
        tank_capacity=60.0,
        max_speed=200,
        fuel_consumption=5.0
    )

    car2 = Vehicle(
        producer='BMW',
        model='M5',
        year=2005,
        tank_capacity=65.0,
        max_speed=150,
        fuel_consumption=7.0
    )

    car3 = Vehicle(
        producer='Dodge',
        model='Viper',
        year=2020,
        tank_capacity=70.0,
        max_speed=300,
        fuel_consumption=10.0
    )

    car1.refueling()
    car2.lend_fuel(car1)
    car3.refueling()
    print(car2.race(150))
    print(car3.race(200))
    car3.lend_fuel(car1)
    car3.lend_fuel(car2)
