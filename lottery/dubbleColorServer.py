#coding=utf-8

'''
双色球的玩法
'''

import random
import time

front = range(1,34)
back = range(1,17)

#上期的开奖结果
lastPeriod4Front=[4,6,9,14,20,29]
lastPeriod4Back = [14]

#144,
filterNo1= [4,14,24]
#20171207,
filterNo2= [7,17,27]
#1020
filterNo3= [10,20,40]

filterNo = filterNo1 + filterNo2 + filterNo3


myBack = [ v for v in back if v not in lastPeriod4Back+lastPeriod4Front+filterNo]
#print myBack
myFront = [ v  for v in front if v not in lastPeriod4Front + lastPeriod4Back+ filterNo]
#print myFront

#14:16 12
for i in range(5):
    print random.sample(myFront, 6),random.sample(myBack,1)
    time.sleep(5)
    
    


