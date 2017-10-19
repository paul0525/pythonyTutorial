#codnig=utf-8
'''
高阶函数，接受函数为参数，或把函数作为结果返回的函数
'''

fruits=['strawberry','fig','apple','cherry','raspberry','banana']

sorted_result = sorted(fruits,key=len)

print sorted_result
print fruits

print sorted(fruits, reverse=True)
print sorted(fruits, reverse=False)



def reverse(word):
    return word[::-1]

print 'testing ->',reverse('testing')

print sorted(fruits,key=reverse)

'''
内置的归约函数
'''
from functools import reduce
from operator import add

print reduce(add,range(100))
print sum(range(100))

'''callable函数,检查对像是否可调用'''
print [callable(obj) for obj in (abs,str,13)]
