'''
1. Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
которая возвращает количество лошидиных сил для автомобиля
2. Создайте наследника класса Car - класс Nissan и переопределите свойство price,
а также переопределите функцию horse_powers
3. Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
а также переопределите функцию horse_powers
'''


class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def horse_powers(self):
        return 0


class Kia(Car):
    price = 3500000

    def horse_powers(self):
        return 360


class Nissan(Car):
    price = 2500000

    def horse_powers(self):
        return 185


optima = Kia(name='Optima')
res = optima.horse_powers()
print(optima.price)
print(res)

almera = Nissan(name='Almera')
res_2 = almera.horse_powers()
print(almera.price)
print(res)