#coding=utf-8
from demo8_c import clock
import functools

"""
使用缓存技术，速度更快
"""

@clock
def finbonacci(n):
    if n < 2:
        return n
    return finbonacci(n-2) + finbonacci(n-1)

if __name__ == '__main__':
    print finbonacci(6)
