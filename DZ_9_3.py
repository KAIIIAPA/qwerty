'''
Задание
1. Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
При создании и инициализации объекта этого класса создаются атрибуты:
- start – начальное значение (если значение не передано, то 0)
- end – конечное значение (если значение не передано, то 1)
'''

class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.n = 0

    def __iter__(self):
        if self.start == 0:
            self.n = 0
        elif self.start % 2 == 0:
            self.n = self.start - 2
        elif self.start % 2 != 0:
            self.n = self.start - 1
        return self

    def __next__(self):
        self.n += 2
        if self.n > self.end:
            raise StopIteration()
        return self.n


res = EvenNumbers(10, 25)
for i in res:
    print(i)
