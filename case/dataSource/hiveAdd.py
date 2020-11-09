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
from comm.sql import Dbconnect
import time
from selenium.webdriver.common.action_chains import ActionChains
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')

sheetName = 'hiveAdd'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()


@ddt.ddt
class HiveAdd(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_hiveAdd(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataAssert','dataAssert_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSource_click').wait_click()
        Element(self.driver,'dataAssert','dataSourcedefault_click').wait_send_keys(data["defaultdataSource_name"])
        time.sleep(2)
        Element(self.driver, 'dataAssert', 'dataSourcedefault_find_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourcedefault_look_click').wait_click()
        time.sleep(1)
        #动态获取默认数据源的用户名和url的值信息
        # Element(self.driver, 'dataAssert', 'dataSourcedefaultname_click').wait_click()
        # time.sleep(1)
        user = Element(self.driver,'dataAssert', 'dataSourcedefaultname_click').get_attribute2()
        # Element(self.driver, 'dataAssert', 'dataSourcedefaulturl_click').wait_click()
        # time.sleep(1)
        url = Element(self.driver,'dataAssert','dataSourcedefaulturl_click').get_attribute2()
        print('user的值是{}，url值是{}'.format(user,url))
        Element(self.driver, 'dataAssert', 'dataSource2_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceAddhive_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceAddhivepre_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver,'dataAssert','dataSourceAddhivename_click').wait_send_keys(data["dataSource_name"]+date)
        Element(self.driver, 'dataAssert', 'dataSourceAddhivedesc_click').wait_send_keys(date+data["dataSouce_desc"])
        Element(self.driver, 'dataAssert', 'dataSourceAddhiveurl_click').wait_send_keys(url)
        Element(self.driver,'dataAssert','dataSourceAddhiveuser_click').wait_send_keys(user)
        Element(self.driver,'dataAssert','dataSourceAddhivepwd_click').wait_send_keys(data["dataSource_pwd"])
        Element(self.driver,'dataAssert','dataSourceAddhiveconnect_click').wait_click()
        # Element(self.driver, 'dataAssert', 'dataSourceAddhiveconnect_click').wait_not_click()
        current_url = Element(self.driver, 'dataAssert', 'dataSourceAddhivesave_click').wait_click()
        time.sleep(1)

        try:
            self.check_result(current_url,data['expect_url1'])
        except:
            return

    @ddt.data(*testData)
    def check_result(self,acual_url,expect_url):
        if int(testData["result"]) == 0:
            assert (acual_url != expect_url)
        else:
            assert (acual_url == expect_url)



    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()