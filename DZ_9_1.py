'''
Цель работы:
    Освоить механизмы работы встроенных функций map и filter. Закрепить их различия и узнать,
    как передавать пользовательскую функцию, как аргумент в функции map и filter.
Задание:
    Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
Примечание:
    Не забывайте, что встроенные функции map и filter возвращают генератор, сами операции преобразования не выполняются.
Входные данные:
    [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
Выходные данные:
    [1, 25, 49, 121, 1225, 7921]
'''
my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def up_number(a):
    return a ** 2

def is_odd(a):
    return a % 2 != 0

res = map(up_number, filter(is_odd, my_numbers))
print(list(res))