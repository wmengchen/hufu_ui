#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 17:30 
# @name: sql
# @author：menghuan.wmc
import os,sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from config import setting
from pymysql.err import OperationalError
import configparser as cpg
from pymysql import connect,cursors

#读取配置文件中的db信息
cpg = cpg.RawConfigParser()
t = cpg.read(setting.Test_config,encoding='utf-8')
host = cpg.get('test_mysqlconf','host')
port = cpg.get('test_mysqlconf','port')
user = cpg.get('test_mysqlconf','user')
pwd = cpg.get('test_mysqlconf','password')
db = cpg.get('test_mysqlconf','db_name')

class Dbconnect():

    def __init__(self):
        try:
            self.conn = connect(host=host,
                                port=int(port),
                                user=user,
                                password=pwd,
                                db=db,
                                cursorclass = cursors.DictCursor
                                )
        except OperationalError as e:
            print('Mysql Error %d :%s'%(e.args[0]),e.args[1])
    def read_config(self,section,key):
        value = cpg.get(section,key)
        print(value)
        return value


    def sql_ProjectInfo(self,section,key):
        with self.conn.cursor()as cursor:
            cursor.execute(self.read_config(section,key).strip("'"))
            #查询的条数
            count = cursor.rowcount
            self.conn.commit()
            return count


if __name__=="__main__":
    db = Dbconnect()
    t  = db.sql_ProjectInfo('sql_find','project')
    print('t的类型是',type(t))



