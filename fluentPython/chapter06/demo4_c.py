#codnig=utf-8
"""
Ѱ������ۿ�
1,���캯������ؽأ�
2,��θ����캯����Ĭ��ֵ��
3,��ε��������������
4, from x import x �� import x ������ ��
"""
#from demo2_c import Customer,LineItem,Order,fidelity_promo,bulk_item_promo, large_order_promo
from demo2_c import *
# import demo2_c   ʹ�õ�ʱ��Ҫ�� module��

promos = [ fidelity_promo,  bulk_item_promo, large_order_promo]

def best_promo(order):
    """
    ѡ����õ�����ۿ�
    """
    return max(promo(order) for promo in promos)


joe1 = Customer('Jonh Doe', 0 )
ann1 = Customer('Ann Smith',2200)

cart1 = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print 'Order4', Order(joe1,cart1, best_promo ) 
print 'Order4', Order(ann1,cart1, best_promo )