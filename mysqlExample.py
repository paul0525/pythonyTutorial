#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''

import MySQLdb

#找开数据库连接
db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","testdb")

#使用cursor()方法获取操作游标
cursor = db.cursor()

#使用execute访求执行sql语句
cursor.execute("select version()")

#使用 fetchone()方法获取一条数据 
data = cursor.fetchone()

print "Database version:%s" % data

#关闭数据库
db.close()