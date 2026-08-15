from account import Account
from abc import ABC, abstractmethod

class WithdrawableAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount):
        pass