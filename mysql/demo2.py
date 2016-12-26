#!/bin/env  python
# coding=utf-8

import MySQLdb as mdb

# 获取数据库的链接对象
con = mdb.connect('localhost', 'root', 'root', 'test', charset='utf8')

with con:
    # 获取普通的查询cursor
    cur = con.cursor()
    tableName = 'mysql_org_device_detail'
    sql = " select COLUMN_NAME from information_schema.COLUMNS  where table_name= '%s'" % (tableName)
    print sql
    cur.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name= '%s'" % (tableName))

    rows = cur.fetchall()

    for rowName in rows:
        print "%s" % rowName[0]