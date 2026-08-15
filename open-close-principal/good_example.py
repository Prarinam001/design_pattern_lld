from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount:int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")
        print("UPI payment processed successfully")

class DebitCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing debit card payment of {amount}")
        print("Debit card payment processed successfully")


class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing net banking payment of {amount}")
        print("Net banking payment processed successfully")

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount: int):
        payment_method.pay(amount)


debit_card_payment = DebitCardPayment()
upi_payment = UPIPayment()
net_banking_payment = NetBankingPayment()


payment_processor = PaymentProcessor()


payment_processor.process_payment(debit_card_payment, 100)
payment_processor.process_payment(upi_payment, 200)
