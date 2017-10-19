#coding=utf-8

from abc import ABCMeta, abstractmethod
from collections import namedtuple

Customer  = namedtuple('Customer', 'name fidelity')

class LineItem:
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity


class Order: #上下文
    
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum( item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            