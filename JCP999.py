#coding=utf-8
'''
Created on 2017年8月14日
python的作用域
@author: dongzhiguo
'''
'''
if 1 ==1 :
    name ='paul'
print(name)


for i in range(10):
    age = i;
    
print(age)
'''

'''
name = "paul"
def f1():
    name = "Eric"
    def f2():
        name = "Snor"
        print(name)
    f2()

f1()
'''

'''
name="lzl"

def f1():
    print(name)

def f2():
    name = "eric"
    f1()

f2()
'''

li = [lambda : x for x in range(10)]
 
res = li[0]()
print(res)


b = lambda x:x+1
print b(10)