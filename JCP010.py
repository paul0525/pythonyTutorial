#coding=utf-8
'''
Created on 2017年8月14日

@author: dongzhiguo
'''

import sys
for i in range(8):
    for j in range(8):
        if(i + j )%2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write('')
        print''