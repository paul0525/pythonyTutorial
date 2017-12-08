#coding=utf-8

'''
大乐透的玩法
'''

import random

front = range(1,36)
back = range(1,13)

#上期的开奖结果
lastPeriod4Front=[1,5,16,19,28]
lastPeriod4Back = [2,10]

myBack = [ v for v in back if v not in lastPeriod4Back+lastPeriod4Front]
#print myBack
myFront = [ v  for v in front if v not in lastPeriod4Front + lastPeriod4Back]
#print myFront


for i in range(5):
    print random.sample(myFront, 5),random.sample(myBack,2)

    


