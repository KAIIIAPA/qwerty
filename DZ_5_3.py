'''
1. Создайте новый класс Buiding
2. Создайте инициализатор для класса Buiding,
который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
3. Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
4. Полученный код напишите в ответ к домашему заданию
'''

class Buiding():

    def __init__(self, numberOfFloors=1, buildingType='старт'):
        self.floors = numberOfFloors
        self.building =buildingType

    def __eq__(self, other):
        print (self.floors == other.floors)
        print (self.building == other.building)

building_1 = Buiding(numberOfFloors=6, buildingType='вверх')
building_2 = Buiding(numberOfFloors=7, buildingType='вверх')

print(building_1 == building_2)