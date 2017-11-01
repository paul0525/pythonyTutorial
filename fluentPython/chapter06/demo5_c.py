#coding=utf-8
"""
从模块中找出合部的策略
"""

from demo2_c import Customer,LineItem,Order,fidelity_promo,bulk_item_promo, large_order_promo



def best_promo(order):
    """
    选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos )


promos = [globals()[name] for name in globals() 
          if name.endswith('_promo') and name != 'best_promo']

joe5 = Customer('Jonh Doe', 0 )
ann5 = Customer('Ann Smith',2200)

cart5 = [LineItem('banana', 4, .5),
         LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print 'Order5', Order(joe5,cart5, best_promo ) 
print 'Order5', Order(ann5,cart5, best_promo )