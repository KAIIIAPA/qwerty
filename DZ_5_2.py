'''
1. Создайте новый класс House
2. Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
3. Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
4. Полученный код напишите в ответ к домашему заданию
'''

class House:

    def __init__(self):
        self.numberOfFloors = 0
        self.count_1 = ['0', ] # на каком этаже лифт изначально

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        self.count_1.append(str(floors)) # складываем список на каких этжах был лифт
        print(f'Этаж №{self.numberOfFloors}')

    def __len__(self):
        print (f'Лифт был на {str(len(self.count_1))} этажах')

    def count_floors(self):
        print ('Лифт побывал на ' + str(len(self.count_1)) + ' этажах, а именно: ' + ', '.join(self.count_1) + '.')

house_1 = House()
house_1.setNewNumberOfFloors(floors=15)
house_1.setNewNumberOfFloors(floors=8)
house_1.setNewNumberOfFloors(floors=5)
house_1.count_floors()
house_1.__len__()