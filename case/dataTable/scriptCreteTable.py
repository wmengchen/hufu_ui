#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/23 15:07 
# @name: scriptCreteTable
# @author：menghuan.wmc


import ddt,unittest,sys,os,re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from selenium.webdriver.common.keys import Keys
from comm.sql import Dbconnect
import time
from selenium.webdriver.common.action_chains import ActionChains

sheetName = 'scriptCreteTable'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()
for item in testData:
     username = item['username']
     password = item['password']

@ddt.ddt
class ScriptCreteTable(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_ScriptCreteTable(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataAssert','dataAssert_click').wait_click()
        Element(self.driver,'dataTable','dataTable_click').wait_click()
        Element(self.driver,'dataTable','dataTablescriptcreateTable_click').wait_click()
        Element(self.driver,'dataTable','dataTableScript_inputclick').wait_click()
        ActionChains(self.driver).send_keys(data["script"]).perform()
        time.sleep(1)
        Element(self.driver,'dataTable','dataTableScript_cancelclick').wait_click()
        time.sleep(2)
        Element(self.driver, 'dataTable', 'dataTablescriptcreateTable_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataTable', 'dataTableScript_inputclick').wait_click()
        ActionChains(self.driver).send_keys(data["script"]).perform()
        time.sleep(1)
        Element(self.driver,'dataTable','dataTableScript_saveclick').wait_click()
        Element(self.driver, 'dataTable', 'dataTableScript_saveclick').wait_not_click()
        time.sleep(1)
        Element(self.driver,'dataTable','dataTablefind_click').wait_send_keys(data["table_name"])
        time.sleep(1)
        content = Element(self.driver,'dataTable','dataTablefind_totalclick').get_text_value()

        self.check_result(content)



    def check_result(self,content):
        number = re.findall(r"\d+\.?\d*", content)
        print("number:",number[0])
        s = number[0]
        print("s的值是",s)

        assert  int(s) == 1




    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()