'''
Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.

Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
чтобы выполнить свою защитную миссию для королевства.
Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
Чем выше умение, тем быстрее рыцарь защитит королевство.
'''
import time
from threading import Thread


class Kingdom(Thread):
    def __init__(self, name, skill):
        super(Kingdom, self).__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name} на нас напали!')
        time.sleep(1)
        while True:
            if self.enemies > 0:
                self.enemies -= self.skill
                self.days += 1
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.', flush=True)
                time.sleep(1)
            else:
                print(f'{self.name} одержал победу спустя {self.days} дней!')
                break


knight1 = Kingdom(name='Sir Lancelot', skill=10)
knight2 = Kingdom(name='Sir Galahat', skill=20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()
