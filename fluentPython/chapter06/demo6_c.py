#coding=utf-8
"""
老感觉这样写不习惯，尤其调用有参数的function
"""
import inspect
import demo6_1_c
from collections import namedtuple

promos= [func for name, func in inspect.getmembers(demo6_1_c, inspect.isfunction)]

def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)



Customer  = namedtuple('Customer', 'name fidelity')

joe6 = Customer('Jonh Doe', 0 )
ann6 = Customer('Ann Smith',2200)

cart6 = [demo6_1_c.LineItem('banana', 4, .5),
         demo6_1_c.LineItem('apple', 10, 1.5),
         demo6_1_c.LineItem('watermellon', 5, 5.0)]

print 'Order6', demo6_1_c.Order(joe6,cart6, best_promo ) 
print 'Order6', demo6_1_c.Order(ann6,cart6, best_promo )