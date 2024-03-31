'''
1. Импортируйте модуль warnings.
2. Реализуйте функцию для расчёта деления, которая будет генерировать предупреждение, если делитель близок к нулю
(например, меньше 0.01), предупреждая об опасности деления на ноль.
3. Сгенерируйте UserWarning в этом случае.
4. Используйте разные фильтры для управления поведением программы при появлении такого предупреждения:
always, ignore, error
'''
import warnings


def division_calculation(number):
    for i in range (number, 0, -1):
        if i <= 1:
            warnings.warn('Предупреждаю об опасности деления на ноль', category=UserWarning)
        res = 1 / i
        if res > 0.20:
            warnings.warn('Предупреждаю результат больше 0.20', category=FutureWarning)
        print(res)


warnings.simplefilter('ignore', FutureWarning) 
division_calculation(number=5)