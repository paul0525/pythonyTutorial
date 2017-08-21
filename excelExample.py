#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''

import xlrd
import xlwt

from datetime import date, datetime

#print datetime.now()
workbook = xlrd.open_workbook(r'D:\temp\ruiyinxing\temp.xlsx')
#print datetime.now()

print workbook.sheet_names()

sheet1 = workbook.sheets()[0]

rowNum = sheet1.nrows
print '行数:%d' % (rowNum)


print '-- for loop begin --'
for i in range(1,rowNum):
    for  item in sheet1.row_values(i):
        print item ,
    print
print '-- for loop end --'    

i = 0
for row  in sheet1.get_rows():
    i +=1
    if i == 1 : 
        continue
    print row
    