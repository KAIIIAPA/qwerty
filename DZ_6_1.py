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
        self.horse_powers_car = 0

    def horse_powers(self):
        self.horse_powers_car = 115
        return

    def __str__(self):
        return '{} {} - {} лошадинных сил, его стоимость составляет {} рублей'.format(
            self.__class__.__name__, self.name, self.horse_powers_car, self.price
        )


class Kia(Car):
    price = 3500000

    def horse_powers(self):
        self.horse_powers_car = 360
        return


class Nissan(Car):
    price = 2500000

    def horse_powers(self):
        self.horse_powers_car = 185
        return


optima = Kia(name='Optima')
optima.horse_powers()
print(optima)

almera = Nissan(name='Almera')
almera.horse_powers()
print(almera)