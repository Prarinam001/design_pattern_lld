from account import Account

class FixedDepositAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount} into fixed deposit account. New balance: {self.balance}")
        