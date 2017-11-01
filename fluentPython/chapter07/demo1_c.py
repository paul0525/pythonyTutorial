#coding=utf-8

"""第一种写法

@decorate
def target():
    print 'running target()'

target = decorate(target)
print target
"""

"""
第二种写法也不对
def target():
    print 'running target()'

target = decorate(target)
print target

"""

def deco(func):
    def inner():
        print 'running innser()'
    return inner

@deco
def target():
    print 'running target()'

print target()
"""
为什么打印的结果有会None呢？
running innser()
None
"""