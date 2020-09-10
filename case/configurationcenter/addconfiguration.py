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



sheetName = 'configurationcenter_add'
date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
testData = ReadExcel(setting.Test_case, sheetName).read_data()


@ddt.ddt
class addconfiguration(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_addconfiguration(self, data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver, 'project', 'Projectfind_click').wait_send_keys(date + data["project_name"])
        Element(self.driver, 'project', 'Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver, 'project', 'enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'dataStanard_click').wait_click()
        Element(self.driver, 'dataStanard', 'configuration_click').wait_click()
        Element(self.driver, 'dataStanard', 'configuration_addclick').wait_click()
        Element(self.driver, 'dataStanard', 'configurationadd_nameclick').wait_send_keys(data["configuration_name"])
        Element(self.driver, 'dataStanard', 'configurationadd_cancelclick').wait_click()
        Element(self.driver, 'dataStanard', 'configuration_click').wait_click()
        Element(self.driver, 'dataStanard', 'configuration_addclick').wait_click()
        Element(self.driver, 'dataStanard', 'configurationadd_nameclick').wait_send_keys(data["configuration_name"])
        Element(self.driver,'dataStanard','configurationadd_okclick').wait_click()
        try:
            Element(self.driver, 'dataStanard', 'configurationadd_okclick').wait_not_click()

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()


if __name__ == "__main__":
    unittest.main()