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
import time



sheetName = 'addDataQuality'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()
for item in testData:
     username = item['username']
     password = item['password']

@ddt.ddt
class addDataQuality(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_addDataQuality(self,data):

        print('---------{}---------'.format(data['case_name']))
        #
        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        # Element(self.driver,'project','Projectfind_click').wait_send_keys(data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        Element(self.driver,'dataQuality','dataQuality_click').wait_click()
        Element(self.driver, 'dataQuality', 'regularManager_click').wait_click()
        Element(self.driver, 'dataQuality', 'table_seachinputclick').wait_send_keys(data["table_name"])
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'table_seachclick').wait_click()
        time.sleep(2)
        Element(self.driver, 'dataQuality', 'monitor_addclick').wait_click()

        Element(self.driver, 'dataQuality', 'partitionexpression_searchclick').wait_send_keys(
            data["partitionexpression"])
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'partitionexpression_searchokclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'regular_addclick').wait_click()
        Element(self.driver, 'dataQuality', 'regular_nameclick').wait_send_keys(data["regular_name"])
        Element(self.driver, 'dataQuality', 'regular_samllclick').wait_click()
        Element(self.driver, 'dataQuality', 'regular_stronglclick').wait_click()
        Element(self.driver, 'dataQuality', 'regular_samllclick').wait_click()
        Element(self.driver, 'dataQuality', 'regularSource_click').wait_click()
        Element(self.driver, 'dataQuality', 'regularinit_click').wait_click()
        Element(self.driver, 'dataQuality', 'regulartype_click').wait_click()
        Element(self.driver, 'dataQuality', 'regulartype_chooseclick').wait_click()
        Element(self.driver, 'dataQuality', 'regularpara_click').wait_click()
        Element(self.driver, 'dataQuality', 'regularpara1_chooseclick').wait_click()
        Element(self.driver, 'dataQuality', 'regularmodel_click').wait_click()
        # time.sleep(1)
        # value = Element(self.driver, 'dataQuality', 'regular_getclick').get_attribute2()
        # print('value的值是：',value)
        # element = get_el_dict('dataQuality', 'regular_getclick')
        # element.find



    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()