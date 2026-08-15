class PaymentProcessor:
    def pay(self, payment_method: str, amount: int):
        if payment_method == "credit_card":
            print(f"Processing credit card payment of {amount}")
            print(f"{payment_method} payment processed successfully")
        elif payment_method == "UPI":
            print(f"Processing UPI payment of {amount}")
            print(f"{payment_method} payment processed successfully")
        elif payment_method == "net_banking":
            print(f"Processing net banking payment of {amount}")
            print(f"{payment_method} payment processed successfully")

payment_processor = PaymentProcessor()
payment_processor.pay("credit_card", 100)