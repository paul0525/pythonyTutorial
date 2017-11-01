#coding=utf-8

promos=[]

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity( order):
    """为积分1000或以上的顾客提供5%折扣"""
    return order.total()*0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item( order ):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_item( order ):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""
    pass


def best_promo( order ):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
    