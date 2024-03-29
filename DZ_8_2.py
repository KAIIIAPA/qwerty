'''
1. Создайте новый проект или продолжите работу в текущем проекте.
2. Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
Например, InvalidDataException и ProcessingException.
'''
class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass
try:
    raise InvalidDataException('игра с мячом и 11 игракоми в каждой команде')
except InvalidDataException as exc:
    print(f'Футбол - это {exc}')
    raise ProcessingException('Это не баскетбол')


'''
3. Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
4. Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
5. В основной части программы вызовите эти функции и корректно обработайте
'''

def example_1(name):

    if name == 'Ildar':
        raise BaseException("Ildar is not teacher")
    print(f'{name} is teacher')


example_1('Denis')
example_1('Ildar')

