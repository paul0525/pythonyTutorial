#coding=utf-8
'''
Created on 2017年8月14日

@author: dongzhiguo
'''

score = int(raw_input('input score:\n'))

if score >= 90:
    grade='A'
elif score >= 60:
    grade = 'B'
else:
    grade='C'

print '%d belongs to %s' % (score, grade)