from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    # @abstractmethod
    # def withdraw(self, amount: float):
    #     pass

    @abstractmethod
    def deposit(self, balance: float):
        pass