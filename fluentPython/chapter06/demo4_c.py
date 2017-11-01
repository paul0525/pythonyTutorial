#codnig=utf-8
"""
寻打最大折扣
1,构造函数如何重截？
2,如何给构造函数赋默认值？
3,如何导入所的类或函数？
4, from x import x 和 import x 的区别 ？
"""
#from demo2_c import Customer,LineItem,Order,fidelity_promo,bulk_item_promo, large_order_promo
from demo2_c import *
# import demo2_c   使用的时候要加 module名

promos = [ fidelity_promo,  bulk_item_promo, large_order_promo]

def best_promo(order):
    """
    选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)


joe1 = Customer('Jonh Doe', 0 )
ann1 = Customer('Ann Smith',2200)

cart1 = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print 'Order4', Order(joe1,cart1, best_promo ) 
print 'Order4', Order(ann1,cart1, best_promo )