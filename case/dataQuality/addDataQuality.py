#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/9/1 14:59
# @name: qualityAdd
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
from selenium.webdriver.common.action_chains import ActionChains
from comm.element import get_el_dict


sheetName = 'addDataQuality'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()

@ddt.ddt
class addDataQuality(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_addDataQuality(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        Element(self.driver,'dataQuality','dataQuality_click').wait_click()
        Element(self.driver, 'dataQuality', 'regularManager_click').wait_click()
        Element(self.driver, 'dataQuality', 'table_seachinputclick').wait_send_keys(data["table_name"])
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'table_seachclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'monitor_addclick').wait_click()


        Element(self.driver, 'dataQuality', 'partitionexpression_searchclick').wait_send_keys(
            data["partitionexpression"])
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'partitionexpression_searchokclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'partitionexpression_searchokclick').wait_click()




    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()