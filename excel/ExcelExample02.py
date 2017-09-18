#coding = utf-8

import xlrd
import xlwt

from LogRecord import LogRecord

def generateLogRecord( beginLine):
     line = beginLine.split(",")
     beginTime = line[0].split(":")[-1].replace("\n","")
     endTime = line[1].split(":")[-1].replace("\n","")
     fileName = line[2].split(":")[-1].replace("\n","")
     return LogRecord(fileName, beginTime, endTime)

f = open('e:/temp.log')
records=[]
beginLine = f.readline()
while beginLine:
     records.append(generateLogRecord(beginLine))
     beginLine = f.readline()
f.close

#Ð´³Éexcel
workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("sheet1",cell_overwrite_ok=True)

worksheet.write(0,0,'applyId')
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

workbook.save("e:/temp_result.xls")
print 'end operated'




