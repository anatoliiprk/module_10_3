import threading
import random
import time

print('------\nЗадача "Банковские операции"\n------')

class Bank:
    def __init__(self, balance: int, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        transaction = 100
        if self.balance >= 500 and self.lock.locked() == True:
            self.lock.release()
        for i in range(transaction):
            amount_d = random.randint(50, 500)
            self.balance += amount_d
            i += 1
            print(f'Пополнение: {amount_d}. Баланс: {self.balance}.')
            time.sleep(0.1)

    def take(self):
        transaction = 100
        for j in range(transaction):
            amount_t = random.randint(50, 500)
            print(f'Запрос на {amount_t}')
            if amount_t <= self.balance:
                self.balance -= amount_t
                print(f'Снятие:{amount_t}. Баланс: {self.balance}.')
                time.sleep(0.1)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            j += 1

bk = Bank(250, False)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}.')

print('------')