'''
Задание:
Напишите 2 функции:
1. Функция, которая складывает 3 числа (sum_three)
2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
"Составное" в противном случае.
'''
def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        count = 0
        for i in range(1, res+1):
            if res % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for number in args:
        total += number
    return total


result = sum_three(2, 3, 6)
print(result)