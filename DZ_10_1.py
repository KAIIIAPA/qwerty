from time import sleep
from threading import Thread
'''
Задание:
1. Напишите программу, которая создает два потока.
2. Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
3. Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
4. Оба потока должны работать параллельно.
'''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def numbers_func():
    for i in range(11):
        print(i)
        sleep(1)

def letters_func():
    for i in letters:
        print(i, flush=True)
        sleep(1)


num_1 = Thread(target=numbers_func)
let_1 = Thread(target=letters_func)

num_1.start()
let_1.start()


num_1.join()
let_1.join()
