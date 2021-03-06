#coding = utf-8

import xlrd
import xlwt

from LogRecord import LogRecord

def generateLogRecord( beginLine, endLine):
     fileName = beginLine.split(":")[0]
     beginTime = beginLine.split("\x9a")[-1].replace("\n","")
     endTime = endLine.split("\x9a")[-1].replace("\n","")
     return LogRecord(fileName, beginTime, endTime)

f = open('e:/chanelTime_direct_result.log')
records=[]
beginLine = f.readline()
endLine = f.readline()
while beginLine:
     records.append(generateLogRecord(beginLine, endLine))
     beginLine = f.readline()
     endLine = f.readline()
f.close

#д��excel
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

workbook.save("e:\chanelTime_direct_result.xls")
print 'end operated'




