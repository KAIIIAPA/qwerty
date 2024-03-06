'''
1. Создайте новый класс Buiding с атрибутом total
2. Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества
созданных объектов класса Building total (по примеру класса Lemming из урока)
3. В цикле создайте 40 объектов класса Building и выведите их на экран командой print
4. Полученный код напишите в ответ к домашему заданию
'''

class Building:

    total = 0

    def __init__(self):
        Building.total += 1

floors = []
for floor in range (1, 41):
    new_floor = Building()
    floors.append(new_floor)

print(len(floors))
print(Building.total)
print(floors)

