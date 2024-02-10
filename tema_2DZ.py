# Ваша задача в файле main.py:
# Создайте новую функцию def test...
# Создайте две переменные a и b внутри пространства имен функции test
# Распечатайте a и b внутри функции test

def test():
    name = 'Ильдар'  # вместа a создал name
    age = 27  # вместо b создал age
    print(name, age)


test()


# Создайте функцию def test2 с тремя параметрами, функция должна распечатывать все три параметра внутри своего тела
# В ответ прикрепите получившийся файл main.py

# Вариант 1
def test2(name2, age2, year_of_birth):
    print(name2, age2, year_of_birth)


test2(name2='Ильдар', age2=27, year_of_birth=1996)


# Вариант 2
def test_2():
    name_2 = 'Ильдар'
    age_2 = 27
    year_of_birth_2 = 1996
    print(name_2, age_2, year_of_birth_2)


test_2()
