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


sheetName = 'addpartitionExpression'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()

@ddt.ddt
class addpartitionExpression(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_addpartitionExpression(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        Element(self.driver,'dataQuality','dataQuality_click').wait_click()
        Element(self.driver, 'dataQuality', 'regularManager_click').wait_click()
        time.sleep(2)
        Element(self.driver, 'dataQuality', 'table_seachinputclick').wait_send_keys(data["table_name"])
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'table_seachclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'monitor_addclick').wait_click()
        Element(self.driver, 'dataQuality', 'partitionexpression_addclick').wait_click()

        Element(self.driver, 'dataQuality', 'partitionexpression_nameclick').wait_send_keys(data["partitionexpression"])
        Element(self.driver, 'dataQuality', 'partitionexpression_okclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataQuality', 'partitionexpression_successclick').wait_click()
        value= Element(self.driver, 'dataQuality', 'partitionexpression_successclick').get_attribute2()
        print('value的值是：',value)
        if value == '请求成功':

            Element(self.driver, 'dataQuality', 'partitionexpression_searchclick').wait_send_keys(
                data["partitionexpression"])
            time.sleep(1)
            Element(self.driver, 'dataQuality', 'partitionexpression_searchokclick').wait_click()
            time.sleep(1)

            element = get_el_dict('dataQuality', 'partitionexpression_moveclick')
            pathValue = element.get('pathValue')
            test = self.driver.find_element_by_xpath(pathValue)
            # 右键到编辑分区表达式界面
            ActionChains(self.driver).move_to_element(test).context_click(test).perform()
            time.sleep(1)
            Element(self.driver,'dataQuality','partitionexpression_editclick').click()
            Element(self.driver, 'dataQuality', 'partitionexpression_editokclick').click()
            time.sleep(2)
            element = get_el_dict('dataQuality', 'partitionexpression_moveclick')
            pathValue = element.get('pathValue')
            test = self.driver.find_element_by_xpath(pathValue)
            # 右键到编辑分区表达式界面
            ActionChains(self.driver).move_to_element(test).context_click(test).perform()
            time.sleep(1)
            Element(self.driver,'dataQuality','partitionexpression_deleteclick').wait_click()
            Element(self.driver, 'dataQuality', 'partitionexpression_editokclick').wait_click()

            time.sleep(2)
            Element(self.driver, 'dataQuality', 'partitionexpression_addclick').wait_click()
            Element(self.driver, 'dataQuality', 'partitionexpression_nameclick').wait_send_keys(
                data["partitionexpression"])
            Element(self.driver, 'dataQuality', 'partitionexpression_okclick').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataQuality', 'partitionexpression_successclick').wait_click()
            value = Element(self.driver, 'dataQuality', 'partitionexpression_successclick').get_attribute2()
            self.assertEqual(value,'请求成功')
        else:
            pass


    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()