#coding=utf-8
"""
实现一个简单的装饰器
"""
import time

def clock( func ):
    def clocked( *args ):
        t0 = time.clock()
        result = func(*args)
        elapsed = time.clock() - t0
        name = func.__name__
        arg_str=','.join(repr(arg) for arg in args)
        print '[%0.8fs] %s(%s) -> %r'%(elapsed, name, arg_str,result)
        return result
    return clocked

        