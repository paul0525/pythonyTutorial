#coding=utf-8
import os 

traveler_ids =[('USA','321879'),('BAR','4589246'),('ESP','CDA25058')]

for passport in traveler_ids:
    print ('%s/%s' % passport)
    

for country,_ in traveler_ids:
    print country

#unpacking
_,filename = os.path.split("d:\python\log.log")
print filename

metro_areas = [\
              ('Tokyo','JP',36.933,(35.89675,-19.9092012)),\
              ('dELHI ncr','MX',36.933,(35.89675,-13.9092012)),\
              ('Mexico City','IN',36.933,(35.89675,139.9092012)),\
              ('New York-Newark','US',36.933,(35.89675,139.9092012)),\
              ('Sao Paulo','BR',36.933,(35.89675,139.9092012))]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}' 
for name ,cc , pop ,(latitude, longitude) in metro_areas:
    if longitude < 0 :
        print (fmt.format(name, latitude,longitude))