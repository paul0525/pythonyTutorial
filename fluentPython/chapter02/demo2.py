#coding=utf-8

#切片
l =[10,20,30,40,50,60]

print l[:2]

print l[:3]

print l[3:]

print l[2:4]


s = 'bicycle'
print s[::3]
print s[::-1]    # elcycib
print s[1:]      # output is icycle
print s[1::-1]   # output is ib
print s[1:0:-1]
print s[1:0:-1]
print s[4:0:-1]
print s[1::2]
print s[-1::-1]  #e
print s[-1:-3:-1]#el
print s[-1:3:-1]  #elc
print s[-3:] #cle
print s[-3::1]   #cle
print s[-1::1]   #e


l = list(range(10))
print l
l[2:5]=[20,30]
print l
del l[5:7]
print l
