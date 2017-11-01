#coding=utf-8
"""
闭包
"""
class Averager():
    
    def __init__(self):
        self.series = []
        
    def __call__(self, new_value):
        self.series.append( new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    series = []
    
    def averager(new_value):
        series.append( new_value )
        total = sum(series)
        return total/len(series)
    return averager


avg = Averager()
print avg(10)
print avg(12)
print avg(13)

print '高阶函数'
avg2 = make_averager()
print avg2(10)
print avg2(12)
print avg2(13)



