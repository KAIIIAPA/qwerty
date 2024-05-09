import inspect

'''
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
   - Тип объекта.
   - Атрибуты объекта.
   - Методы объекта.
   - Модуль, к которому объект принадлежит.
   - Другие интересные свойства объекта, учитывая его тип (по желанию).
'''


class Man():
    def __init__(self, name, age, year_of_birth):
        self.name = name
        self.age = age
        self.year_of_birth = year_of_birth


def introspection_info(obj):
    # получаем тип объекта
    type_name = type(obj).__name__
    # получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__') and attr != '__dict']
    # получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    # получаем модуль к которому принадлежит объект
    module = getattr(obj, '__module__', None) or getattr(type(obj), '__module__', None)

    # Возвращаем словарь с информацией об объекте
    return {
        'type': type_name,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }


number_ = introspection_info(42)
print(number_)

me = Man('Ildar', 28, 1996)
print(introspection_info(me))