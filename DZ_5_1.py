'''
1.Создайте новый класс House
2.Задайте ему новый атрибут numberOfFloors = 10
3.В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
4.Полученный код напишите в ответ к домашему заданию
'''

class House:

    def __init__(self):
        self.numberOfFloors = 10

    def print_1(self):
        print("Текущий этаж равен", self.numberOfFloors)

house_1 = House()
house_1.print_1()

# или

class House_1:

    def __init__(self, numberOfFloors_1):
        self.floor = numberOfFloors_1

    def print_2(self):
        print("Текущий этаж равен", self.floor)


house_2 = House_1(numberOfFloors_1=10)
house_2.print_2()