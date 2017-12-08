#coding=utf-8

import random

red = range(1,34)
blue = range(1,17)

for i in range(20):
    print random.sample(red, 6),random.sample(blue,1)
    
