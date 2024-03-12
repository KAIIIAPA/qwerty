'''
1. Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
2. Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
которая возвращает количество лошидиных сил для автомобиля
3. Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
а также переопределите функцию horse_powers
4. Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
'''


class Vehicle:

    def __init__(self):
        self.vehicle_type = None


class Car:

    def __init__(self):
        self.price = 10000

    def horse_powers(self):
        return '100 лошадинных сил'


class Nissan(Vehicle, Car):

    def __init__(self):
        super().__init__()
        self.price = 2500000
        self.vehicle_type = 'Car'

    def horse_powers(self):
        return '185 лошадинных сил'

Nissan_1 = Nissan()
print(Nissan_1.vehicle_type)
print(Nissan_1.price)

print(Nissan_1.horse_powers())
