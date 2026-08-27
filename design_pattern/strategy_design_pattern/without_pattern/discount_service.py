class DiscountService:
    def calculate_discount(self, discount_type: str):
        if discount_type == "Diwali":
            print("Applying diwali discount of 20%")
        elif discount_type == "First Order":
            print("Applying first order discount of 15%")
        else:
            print("No discount applied")
