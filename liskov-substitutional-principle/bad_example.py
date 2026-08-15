from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance: float):
        super().__init__(balance)

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from savings account. New balance: {self.balance}")
        else:
            print("Insufficient balance in savings account.")
    
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount} into savings account. New balance: {self.balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, balance: float):
        super().__init__(balance)

    def withdraw(self, amount: float):
        print("Withdrawals are not allowed from fixed deposit accounts.")
        raise Exception("Withdrawals are not allowed from fixed deposit accounts.")

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount} into fixed deposit account. New balance: {self.balance}")


s = SavingsAccount(1000)
s.withdraw(200)


fd = FixedDepositAccount(5000)
fd.withdraw(1000)  # This will raise an exception