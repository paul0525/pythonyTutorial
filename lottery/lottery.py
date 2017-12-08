#coding=utf-8
import random

'''
算法：
1）选号的方式有哪些：
    a 先排除（排除红色+蓝色），后随机
    b 和值范围，奇偶数比列
2）统计下出现联号的可能性？
3）统一下上期和下期出现连号的概率？
4）每隔多少期会出现连号？
5) 统计下和值的范围
6） 随机出来的号在历史上有没有？
7) 个位数上相同的情况
8) 是不是要模拟一个官网，然后还有一个客户端

重点：先找出蓝球的规律
'''

#期数 第几期
periodsNo='2017143'

#开奖日期
date='20171206'

#农历日期
lunarDate='20171019'

#上期的开奖结果
lastPeriodResult = (1,2,3,14,16,27,16)


'''
红区被遗弃的数字
1）上期开过的红球可以不开，顶多一两个连球
2）上期的蓝色在红区是否要排除？
3）好几期的蓝色在红区是否要排除？
'''
def getAbandonOfRedNumber():
    pass

'''
蓝区被遗弃的数字
1)找出最近历史上，比方 12 的下期的数字
2)红球里有小于17的一律排除
'''
def getAbandonOfBlueNumber():
    pass


redNum = range(1,34)
blueNum = range(1,17)
print random.sample(redNum,6), random.sample(blueNum, 1)

