#codnig=utf-8
from functools import reduce
from operator import mul

"""º¯Êı±à³ÌÊ½ÓïÑÔ"""

def fact(n):
    return reduce(lambda a,b:a*b,range(1,n+1))

print fact(5)


def fact1(n):
    return reduce(mul, range(1,n+1))


print fact1(5)