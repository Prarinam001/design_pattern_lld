from withdrawable_account import WithdrawableAccount

class SavingsAccount(WithdrawableAccount):
    def __init__(self, amount: float):
        super().__init__(amount)

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from savings account. New balance: {self.balance}")
        else:
            print("Insufficient balance in savings account.")

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount} into savings account. New balance: {self.balance}")