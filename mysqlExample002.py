#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''
import MySQLdb


db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","testdb")

cursor = db.cursor()

#sql插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
         VALUE('MAC','Mohan',20,'M',2000)"""

try:     
    #执行sql语句
    cursor.execute(sql)
    #提交
    db.commit()
except:
    #Rollback in case there is any error
    db.rollback()
    
db.close()
print '数据插入成功'