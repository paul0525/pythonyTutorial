#coding=utf-8
a = [1,3,5,7,9]

print "修改之前的a:%s"%(a)
b = map(lambda x : x*2 , a )

print "修改之后的b:%s"%(b)

'''归并操作'''
print reduce(lambda x,y:x+y, a)