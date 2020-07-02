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
from selenium.webdriver.common.keys import Keys
from comm.sql import Dbconnect
import time

sheetName = 'project'
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()


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

        print('---------{}---------'.format(data['case_name']))
        Element(self.driver,'project','createProject_click').wait_click()
        Element(self.driver,'project','Projectname_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectdesc_click').wait_send_keys(data["project_desc"])
        Element(self.driver,'project','Projectcancel_click').wait_click()
        time.sleep(2)
        Element(self.driver,'project','createProject_click').wait_click()
        Element(self.driver,'project','Projectname_click').wait_send_keys(date + data["project_name"])
        Element(self.driver,'project','Projectdesc_click').wait_send_keys(data["project_desc"])
        Element(self.driver,'project','Projectok_click').wait_click()
        time.sleep(3)
        Element(self.driver, 'project', 'Projectcancel_click').wait_click()
        time.sleep(1)
        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)




    def tearDown(self):
         print('--------测试结束--------')
         self.login.logout()


if __name__=="__main__":
    unittest.main()











