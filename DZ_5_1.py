'''
1.Создайте новый класс House
2.Задайте ему новый атрибут numberOfFloors = 10
3.В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
4.Полученный код напишите в ответ к домашему заданию
'''

# Вариант_1
class House:

    def __init__(self):
        self.numberOfFloors = 10
        self.print_1 = f"Текущий этаж равен {self.numberOfFloors}"

house_1 = House()
print(house_1.print_1)

# Вариант_2

class House_1:

    def __init__(self, numberOfFloors_1):
        self.floor = numberOfFloors_1

    def print_2(self):
        print("Текущий этаж равен", self.floor)


house_2 = House_1(numberOfFloors_1=10)
house_2.print_2()

# Вариант_3
class House:

    def __init__(self):
        self.numberOfFloors = 10

    def print_1(self):
        print("Текущий этаж равен", self.numberOfFloors)

house_1 = House()
house_1.print_1()
