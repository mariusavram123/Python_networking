#!/usr/bin/python3

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Chanu", 1000)

account.deposit(500)

print(account.get_balance())
