from abc import ABC, abstractmethod
from datetime import datetime


def log_time(func):
    def wrapper(*args, **kwargs):
        stsrt_time = datetime.now()
        func()
        end_time = datetime.now()
        print(f'transacyion stsrts at {stsrt_time} and stops at {end_time}')
    return wrapper


class BankAccount(ABC):
    @abstractmethod
    def add_money(self, amount):
        pass
    @abstractmethod
    def payment(self, amount):
        pass
class DepositBankAccount(BankAccount):
    def __init__(self, name,number):
        self.__name = name
        self.__balance = 0
        self.__id = '1234'+str(number)

    @log_time
    def add_money(self, amount):
        self.__balance += amount
        print(f'Client {self.__name} added {amount}. balance is {self.__balance}')

    @log_time
    def payment(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Client {self.__name} added {amount}. balance is {self.__balance}')
        else:
            print(f'not enough money. Balance is {self.__balance}')


class Client:
    def __init__(self, name):
        self.__name = name
        self.accounts = []

    def create_account(self, number):
        new_account = DepositBankAccount(self.__name, number)
        self.accounts.append(new_account)






