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
    def pay(self, order, security_code):
        pass
        
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print("Verifying security code: {security_code}") 
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print("Verifying security code: {security_code}") 
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing Paypal payment type")
        print("Verifying security code: {security_code}") 
        order.status = "paid"
         
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("ssD", 1, 150)
order.add_item("USB Cable", 2, 5)

print (order.total_price())
pp = PaypalPaymentProcessor()
pp.pay(order, "046738")