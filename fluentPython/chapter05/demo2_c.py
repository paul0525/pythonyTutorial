#codnig=utf-8
'''
�߽׺��������ܺ���Ϊ��������Ѻ�����Ϊ������صĺ���
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
���õĹ�Լ����
'''
from functools import reduce
from operator import add

print reduce(add,range(100))
print sum(range(100))

'''callable����,�������Ƿ�ɵ���'''
print [callable(obj) for obj in (abs,str,13)]
