'''
Добавление обработки исключений. К данным функциям добавить как минимум одну обработку указанных типов исключений:
def string_to_int(s): # добавить обработку ValueError
   return int(s)
def read_file(filename): # добавить обработку FileNotFoundError, IOError
with open(filename, 'r') as file:
   return file.read()
def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    return a / b
def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    return lst[index]
'''


def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое число."


res = string_to_int('буква')
print(res)


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileExistsError:
        return f"Ошибка: файл '{filename}' не найден."
    except IOError:
        return f"Ошибка ввода/вывода при работе с файлом '{filename}'"


res_1 = read_file(filename='1234.txt')
print(res_1)


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        print("Ошибка: аргументы должны быть числами")


res_3 = divide_numbers(10, 0)
print(res_3)


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапозона списка."
    except TypeError:
        return f"Ошибка: индекс должен быть целым числом"


res_4 = access_list_element([0, 1, 2, 3, 4], 8)
print(res_4)