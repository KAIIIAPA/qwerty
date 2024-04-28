import time
from threading import Thread, Lock

'''
Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи 
и уходящих после завершения приема.

Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят. 
Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.

Создайте 3 класса:
+ Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, 
+ is_busy(bool) - занят стол или нет.

+ Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
+ Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
+ Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов, 
в случае наличия стола - начинает обслуживание посетителя (запуск потока), 
в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.

Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

Так же должны выводиться текстовые сообщения соответствующие событиям:
Посетитель номер <номер посетителя> прибыл.
Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)
'''


class Table():
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe():
    def __init__(self, tables):
        self.queue_ = []
        self.tables = tables
        self.tables_lock =Lock()
        self.customers = 0

    def customer_arrival(self):
        customer_number = 1
        while True:
            if self.customers < 20:
                time.sleep(1)
                print(f'Посетитель номер {customer_number} прибыл.', flush=True)
                customer = Customer(customer_number, self)
                customer_number += 1
                with self.tables_lock:
                    if self.serve_customer(customer):
                        customer.start()
                    else:
                        self.queue_.append(customer)
                self.customers += 1

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                customer.table = table
                print(f'Посетитель номер {customer.number} сел за стол {table.number}.', flush=True)
                return True
        print(f'Посетитель номер {customer.number} ожидает свободный стол.', flush=True)


class Customer(Thread):

    def __init__(self, number, cafe, table=None):
        Thread.__init__(self)
        self.number = number
        self.cafe_ = cafe
        self.table = table

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушел', flush=True)
        self.table.is_busy = False

        with self.cafe_.tables_lock:
            self.table.is_busy = False
            if self.cafe_.queue_:
                next_customer = self.cafe_.queue_.pop(0)
                self.cafe_.serve_customer(next_customer)
                next_customer.table = self.table
                next_customer.start()



# Создаем столики в кафе
table1 = Table(number=1)
table2 = Table(number=2)
table3 = Table(number=3)

tables_ = [table1, table2, table3]

# Инициализируем кафе

cafe = Cafe(tables=tables_)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

