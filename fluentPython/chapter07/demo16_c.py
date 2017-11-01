#coding=utf-8

import time
from demo15_c import clock


@clock('{name}:{elapsed}s')
def snooze(seconds):
    time.sleep(seconds)
    
for i in range(3):
    snooze(.123)