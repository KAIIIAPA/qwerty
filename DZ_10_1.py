from time import sleep
from threading import Thread
'''
Задание:
1. Напишите программу, которая создает два потока.
2. Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
3. Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
4. Оба потока должны работать параллельно.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def perebor(name, n):
    for i in range (n):
        sleep(1)
        print(name[i], flush=True)


thread = Thread(target=perebor, kwargs=dict(name=numbers, n=10))
thread.start()

perebor(name=letters, n=10)

thread.join()