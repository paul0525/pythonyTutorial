#coding=utf-8

"""
变量作用域规则
"""


def f1(a):
    print(a)
    print(b)

b = 6
f = f1(3)
print f
print 'hello python'