#coding = utf-8

import xlrd
import xlwt

from LogRecord import LogRecord

def generateLogRecord( beginLine, endLine):
     fileName = beginLine.split(":")[0]
     beginTime = beginLine.split("\x9a")[-1].replace("\n","")
     endTime = endLine.split("\x9a")[-1].replace("\n","")
     return LogRecord(fileName, beginTime, endTime)

f = open('D:/channelTime.txt')
records=[]
beginLine = f.readline()
endLine = f.readline()
while beginLine:
     records.append(generateLogRecord(beginLine, endLine))
     beginLine = f.readline()
     endLine = f.readline()
f.close

#写成excel
workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("sheet1",cell_overwrite_ok=True)

worksheet.write(0,0,'fileName')
worksheet.write(0,1,'beginTime')
worksheet.write(0,2,'endTime')
worksheet.write(0,3,'diff')

i = 1
for record in records:
     worksheet.write(i,0,label=record.fileName)
     worksheet.write(i,1, label=record.beginTime)
     worksheet.write(i,2, label=record.endTime)
     diff = str(int(record.endTime)-int(record.beginTime))
     worksheet.write(i,3, label=diff)
     i += 1

workbook.save("d:\channelTime_result.xls")
print 'end operated'

'''
截取字符串

str = 'dubbo20170831112058000001_bankcard_auth2017-08-31.trc:20170831:11:20:58.451 INFO  *****请求开始时间：1504149658451'
arrStr = str.split(":")
print arrStr[0]
arrStr1 = str.split("：")
print arrStr1[-1]
'''


