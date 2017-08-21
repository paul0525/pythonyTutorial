#coding=utf-8
'''
Created on 2017年8月16日

@author: dongzhiguo
'''

class Employee:
    '所有员式的基类'
    empCount = 0 
    
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        
    
    def displayCount(self):
        print ""