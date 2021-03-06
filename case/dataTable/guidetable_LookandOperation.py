# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/24 10:21
# @name: guideCreateTable
# @author：menghuan.wmc

import ddt, unittest, sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from selenium.webdriver.common.keys import Keys
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')
sheetName = 'guidetable_LookandOperation'
date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
testData = ReadExcel(setting.Test_case, sheetName).read_data()


@ddt.ddt
class guidetable_LookandOperation(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_guidetable_LookandOperation(self, data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver, 'project', 'Projectfind_click').wait_send_keys(date + data["project_name"])
        Element(self.driver, 'project', 'Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver, 'project', 'enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'dataStanard_click').wait_click()
        Element(self.driver, 'dataStanard', 'modelDesign_click').wait_click()
        Element(self.driver, 'dataStanard', 'tablesearch_input').wait_send_keys(data["table_name"])
        Element(self.driver, 'dataStanard', 'standard_click').wait_click()
        Element(self.driver, 'dataStanard', 'standard_chooseclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_searchclick').wait_click()
        time.sleep(1)
        value= Element(self.driver, 'dataStanard', 'tablelook_click').is_enabled()
        print('value的值是：',value)
        self.assertTrue(value)
        time.sleep(1)
        value2 = Element(self.driver, 'dataStanard', 'tableoperation_click').is_enabled()
        print("value2:",value2)
        self.assertTrue(value2)
        # Element(self.driver, 'dataStanard', 'tableoperation_okclick').wait_click()
        # time.sleep(1)
        # Element(self.driver, 'dataStanard', 'tablemodeldesign_click').wait_click()
        # self.assertTrue()

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()


if __name__ == "__main__":
    unittest.main()