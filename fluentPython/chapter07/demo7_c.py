#coding=utf-8
"""
nonlocal声明
python2没有nolocal，可以使用dict来替换nonlocal
"""

def make_averager():
    count={}
    count[0] = 0
    total={}
    total[0] = 0
    
    def averager(new_value):
        count[0] += 1
        total[0]  += new_value
        return total[0]/ count[0]
    
    return averager

avg = make_averager()
print avg(10)
print avg(12)
print avg(2)