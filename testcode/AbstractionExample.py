from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}"
    
class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processed Paypal payment of ${amount}"
    

ccPayment = CreditCardPayment()
ppPayment = PayPalPayment()

print(ccPayment.process_payment(100))
print(ppPayment.process_payment(200))