'''
Цель задания:
Повторить тему ООП, применив новые изученные модули даты и времени.
Создать усовершенствованный класс datetime.
Задание:
Создайте класс SuperDate, наследованный от класса datetime модуля datetime,
объекты которого будут дополнительно обладать следующими методами:
1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток
(Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)

Пример работы класса:
a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

Вывод на консоль:
Winter
Day
'''
import datetime


class SuperDate(datetime.datetime):

    def __init__(self, year, month, day, hours):
        self.date_ = datetime.datetime(year=year, month=month, day=day, hour=hours)

    def get_time_of_day(self):
        if 6 <= self.date_.hour <= 11:
            return f'Morning'
        elif 12 <= self.date_.hour <= 17:
            return f'Day'
        elif 18 <= self.date_.hour <= 23:
            return f'Evening'
        else:
            return f'Night'

    def get_season(self):
        if 3 <= self.date_.month <= 5:
            return f'Spring'
        elif 6 <= self.date_.month <= 8:
            return f'Summer'
        elif 9 <= self.date_.month <= 11:
            return f'Autumn'
        else:
            return f'Winter'


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())