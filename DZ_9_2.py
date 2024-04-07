'''
Задание:
Задача 1: Фабрика Функций
Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в зависимости
от переданных аргументов.
'''

def multiplier_z_1(n):
    if n % 2 == 0 and n > 0:
        def calculator(x):
            return x / 2
    elif n % 2 != 0 and n > 0:
        def calculator(x):
            return x * 5
    else:
        raise Exception('Я могу принимать только целочисленные значения больше 0')

    return calculator


my_numbers = [9, 8, 7, 6, 5, 4]
z_1 = multiplier_z_1(n=int(input('Введите число n: ')))
res_1 = map(z_1, my_numbers)
print(list(res_1))

'''
Задача 2: Лямбда-Функции
Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
Например, возведение числа в квадрат
'''

my_numbers = [9, 8, 7, 6, 5, 4]

z_2_1 = map(lambda x: x ** 2, my_numbers)
print(list(z_2_1))

def square(x):
    return x ** 2

z_2_2 = map(square, my_numbers)
print(list(z_2_2))


'''
Задача 3: Вызываемые Объекты
Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь
прямоугольника, то есть a*b.
'''

class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

sqaure_rectangle = Rect(a=int(input('Высота: ')), b=int(input('Ширина: ')))
z_3_1 = sqaure_rectangle()
print(f'Площадь прямоугольника ровна: {z_3_1}')