# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:31:23 2024

@author: gyane
"""
from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"
    
    
    def add_item(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.quantities[i] * self.prices[i]
        return total
    

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    #Problem: This method is not supported by all the child classes e.g. CreditPaymentProcessor. Solution would be to follow the Interface Segregation Priciple and put it in 
    # a different interface
    @abstractmethod
    def auth_sms(self, code):
        pass
        
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verfying SMS code - {code}")
        self.verified = True
        
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}") 
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        
    def auth_sms(self, code):
        raise Exception("Credit card payment type does not support SMS code authorization") #This is a voilation of Liskov Subs Princ
        
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}") 
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code - {code}")
        self.verified = True
        
    def pay(self, order):
        if not self.verified:
            raise Exception("Payment not authorized")
        print("Processing Paypal payment type")
        print(f"Verifying email address: {self.email_address}") 
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("ssD", 1, 150)
order.add_item("USB Cable", 2, 5)

print (order.total_price())
pp = PaypalPaymentProcessor("abc@gmail.com")
pp.auth_sms("1234")
pp.pay(order)