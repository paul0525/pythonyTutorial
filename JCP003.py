#coding=utf-8
'''
Created on 2017年8月14日

@author: dongzhiguo
'''
import math

for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if(x*x ==i+100 ) and ( y*y == i + 268):
        print i