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
from selenium.webdriver.common.action_chains import ActionChains

sheetName = 'relationdataSource'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()


@ddt.ddt
class RelationDb(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_relationDb(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataAssert','dataAssert_click').wait_click()
        Element(self.driver,'dataAssert', 'dataSourceadd_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddMysql_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver,'dataAssert','dataSourceTestConpre_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceTestConpre_click').wait_not_click()
        Element(self.driver,'dataAssert','dataSourceadd_nextclick').wait_click()
        Element(self.driver,'dataAssert','dataSourcename_click').wait_send_keys(data["dataSource_name"]+date)
        Element(self.driver, 'dataAssert', 'dataSourcedesc_click').wait_send_keys(date+data["dataSouce_desc"])
        Element(self.driver, 'dataAssert', 'dataSourceurl_click').wait_send_keys(data["dataSource_url"])
        Element(self.driver,'dataAssert','dataSourceuser_click').wait_send_keys(data["dataSource_user"])
        Element(self.driver,'dataAssert','dataSourcepwd_click').wait_send_keys(data["dataSource_pwd"])
        Element(self.driver,'dataAssert','dataSourceTestCon_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceTestConpre_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceSave_click').wait_click()

        Element(self.driver,'dataAssert','dataSourceok_click').wait_click()
        try:
            Element(self.driver, 'dataAssert', 'dataSourceok_click').wait_not_click()
        except:
            pass
        Element(self.driver,'dataAssert','dataSourcefindname_click').wait_send_keys(data["dataSource_name"]+date)
        Element(self.driver,'dataAssert','dataSourceedit_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataAssert','dataSourcenameedit_click').clear()
        time.sleep(1)
        Element(self.driver, 'dataAssert', 'dataSourcenameedit_click').wait_send_keys(data["edit_sourceName"]+date)
        Element(self.driver, 'dataAssert', 'dataSourceedit_saveclick').wait_click()
        content = Element(self.driver,'dataAssert','dataSourceedit_dataclick').get_text_value()
        print('content的内容是：',content)
        self.check_result(content)
    def check_result(self,content):
        assert content == '共1条'

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()
