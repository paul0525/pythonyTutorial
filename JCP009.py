#coding=utf-8
'''
Created on 2017年8月14日

@author: dongzhiguo
'''

for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print '%d * %d = %-3d'%(i,j,result)
    print''
