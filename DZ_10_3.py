'''
Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions)
при модификации общего ресурса.
'''

import threading


class BankAccount(threading.Thread):

    def __init__(self, amount, n=10):
        super().__init__()
        self.balance = 1000
        self.amount = amount
        self.n = n


def deposit_task(balance, amount, n):
    for i in range(n):
        lock.acquire()
        balance += amount
        print(f'Deposit {amount}, new balance is {balance}')
        lock.release()


def withdraw_task(balance, amount, n):
    for i in range(n):
        lock.acquire()
        balance -= amount
        print(f'Withdraw {amount}, new balance is {balance}')
        lock.release()


lock = threading.Lock()

account_1 = BankAccount(amount=10)

deposit_thread = threading.Thread(target=deposit_task, args=(account_1.balance, account_1.amount, account_1.n))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account_1.balance, account_1.amount, account_1.n))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
