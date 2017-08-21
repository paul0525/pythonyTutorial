#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''
import MySQLdb

db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","testdb")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
         
cursor.execute(sql)
print '表创建成功'
#关闭数据库连接
db.close()

