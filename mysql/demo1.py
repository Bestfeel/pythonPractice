#!/bin/env  python
# coding=utf-8

import MySQLdb as mdb

# 获取数据库的链接对象
con = mdb.connect('localhost', 'root', 'root', 'test', charset='utf8')

with con:
    # 获取普通的查询cursor
    cur = con.cursor()
    tableName = 'mysql_org_device_detail'
    sql = "SELECT * FROM   %s" % (tableName)
    print sql
    cur.execute("SELECT * FROM   %s" % (tableName))
    # rows = cur.fetchall()
    # 获取连接对象的描述信息
    desc = cur.description
    # print 'cur.description:', desc
    # print len(desc)
    for rowName in desc:
        print "%s" % rowName[0]
