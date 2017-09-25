#coding=utf-8

symbols = '$#%&~*'
codes=[]
for symbol in symbols:
    codes.append( ord(symbol) )
print codes


symbols = '$#%&~*'
codes=[ord(symbol) for symbol in symbols]
print codes

colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color, size) for color in colors \
                         for size in sizes ]

print tshirts
