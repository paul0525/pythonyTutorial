#coding=utf-8
"""
函数式编程语言 得益于 operator 和 functools 的支持
"""
metor_data = [
    ('Tokyo','JP',36.933,(35.687221,139.691667)),
    ('Delhi NCR','IN',21.933,(28.687221,77.691667)),
    ('Mexico City','MX',20.142,(19.687221,-99.691667)),
    ('New York-Newark','US',20.104,(40.687221,-74.691667)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.691667)),
]

from operator import itemgetter

for city in sorted(metor_data,key = itemgetter(1)):
    print(city)

cc_name = itemgetter(1,0)

for city in metor_data:
    print(cc_name(city))