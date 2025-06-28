from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid €{amount} using Credit Card ending in {self.card_number[-4:]}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid €{amount} using PayPal account {self.email}.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid €{amount} using Bitcoin.")

# Step 3: Context Class
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)

# Step 4: Usage
if __name__ == "__main__":
    # Choose a payment method
    credit_card = CreditCardPayment("1234-5678-9876-5432")
    paypal = PayPalPayment("user@example.com")
    bitcoin = BitcoinPayment()

    # Create context and execute different strategies
    context = PaymentContext(credit_card)
    context.execute_payment(100)

    context.set_strategy(paypal)
    context.execute_payment(75)

    context.set_strategy(bitcoin)
    context.execute_payment(50)