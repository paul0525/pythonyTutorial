#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''

import MySQLdb

db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","testdb")

cursor = db.cursor()

sql ="update employee set age = age+1 where sex = '%c'" %('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    
db.close()
print '修改成功'