#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 11:16 
# @name: createProject
# @author：menghuan.wmc
import ddt,unittest,sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from comm.sql import Dbconnect
import time

sheetName = 'project'

testData = ReadExcel(setting.Test_case,sheetName).read_data()
time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

@ddt.ddt
class Project(unittest.TestCase):


    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_createProject(self,data):

        print('---------开始执行测试用例:{}---------'.format(data['case_name']))

        Element(self.driver,'project','createProject_click').click()
        Element(self.driver,'project','Projectname_click').send_keys(time+data["project_name"])
        Element(self.driver,'project','Projectdesc_click').send_keys(data["project_desc"])
        Element(self.driver,'project','Projectcancel_click').click()

        Element(self.driver, 'project', 'createProject_click').click()
        Element(self.driver, 'project', 'Projectname_click').send_keys(time + data["project_name"])
        Element(self.driver, 'project', 'Projectdesc_click').send_keys(data["project_desc"])
        Element(self.driver,'project','Projectok_click').click()
        time.sleep(12)

        print('---------结束执行测试用例:{}---------'.format(data["case_name"]))

    def tearDown(self):
         print('--------测试结束--------')
         self.login.logout()
    #
    # def test_editProject(self,data):
    #
    #     Element(self)

if __name__=="__main__":
    unittest.main()











