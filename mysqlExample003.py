#coding=utf-8
'''
Created on 2017年8月15日

@author: dongzhiguo
'''

import MySQLdb

db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","testdb")

cursor= db.cursor()

sql="select * from employee where income > '%d'" % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d")% \
            (fname, lname, age,sex, income)
    
except:
    print "Error: unable to fetch data"

db.close()