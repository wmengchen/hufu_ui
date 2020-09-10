#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/15 16:58
# @name: sqlServerAdd
# @author：menghuan.wmc

import ddt,unittest,sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from selenium.webdriver.common.keys import Keys
import time


sheetName = 'mongoAdd'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()

@ddt.ddt
class MongoAdd(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_mongoAdd(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataAssert','dataAssert_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSource_click').wait_click()
        Element(self.driver,'dataAssert', 'dataSourceadd_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddmondb_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddmondbpre_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddmondbname_click').wait_send_keys(data["dataSource_name"] + date)
        Element(self.driver, 'dataAssert', 'dataSourceaddmondbdesc_click').wait_send_keys(date + data["dataSouce_desc"])
        Element(self.driver,'dataAssert','dataSourceaddmondbserver_click').wait_send_keys(data["url"])
        Element(self.driver,'dataAssert','dataSourceaddmondbDBinfo_click').wait_send_keys(data["db"])
        Element(self.driver,'dataAssert', 'dataSourceaddmondbDBverify_click').wait_send_keys(data['vertifydb'])
        Element(self.driver,'dataAssert','dataSourceaddmondbuser_click').wait_send_keys(data["user"])
        time.sleep(3)
        Element(self.driver, 'dataAssert', 'dataSourceaddmondbpwd_click').wait_send_keys(int(data["pwd"]))
        Element(self.driver, 'dataAssert', 'dataSourceaddmondbconnect_click').wait_click()
        current_url = Element(self.driver, 'dataAssert', 'dataSourceaddmondbsave_click').wait_click()
        time.sleep(1)
        try:
            self.check_result(current_url,data['expect_url1'])
        except:
            return

    @ddt.data(*testData)
    def check_result(self,acual_url,expect_url):
        print('int(testData["result"]):',int(testData["result"]))
        if int(testData["result"]) == 0:
            assert (acual_url != expect_url)
        else:
            assert (acual_url == expect_url)



    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()