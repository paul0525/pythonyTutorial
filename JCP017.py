#coding=utf-8
'''
Created on 2017年8月14日

@author: dongzhiguo
'''

import string
s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space=%d,digit=%d,others=%d'%(letters,space,digit,others)

if not(-1>1):
    print 'hello'