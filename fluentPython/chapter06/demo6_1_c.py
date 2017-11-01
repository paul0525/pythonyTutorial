#coding=utf-8
"""
使用函数实现折扣策略
"""



class LineItem:
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity


class Order: #上下文
    
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum( item.total() for item in self.cart)  #这样的写法要重点记忆
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0 
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(),self.due())

    
    
def fidelity_promo(order):
    """为积分为1000或以上客户提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0
    
def bulk_item_promo(order):
    """单个商品为20或以上时提供10%折扣"""
    discount = 0 
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount    
        
def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = { item.product for item in order.cart }
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

