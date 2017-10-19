#coding=utf-8

metor_data = [
    ('Tokyo','JP',36.933,(35.687221,139.691667)),
    ('Delhi NCR','IN',21.933,(28.687221,77.691667)),
    ('Mexico City','MX',20.142,(19.687221,-99.691667)),
    ('New York-Newark','US',20.104,(40.687221,-74.691667)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.691667)),
]

from collections import namedtuple

LatLong = namedtuple('LatLong','lat long')
Metropolis = namedtuple('Metropolis','name cc pop coord')
metro_areas = [Metropolis(name, cc , pop, LatLong(lat,long))
                    for name, cc, pop, (lat,long) in metro_data]