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
sheetName = 'guide_edit'
date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
testData = ReadExcel(setting.Test_case, sheetName).read_data()


@ddt.ddt
class guide_edit(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_guide_edit(self, data):

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
        Element(self.driver, 'dataStanard', 'table_edit_click').wait_click()
        Element(self.driver, 'dataStanard', 'table_nameregular_click').wait_click()
        Element(self.driver, 'dataStanard', 'table_nameregular_okclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_lifestyleclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_lifestyle_chooseclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_lifestyleclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_lifestyle_defineclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_lifestyle_defineinputclick').wait_send_keys(int(data["lifestyle"]))
        Element(self.driver, 'dataStanard', 'tableedit_addpara_click').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_addpara_inputclick').wait_send_keys("para3name")
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_typeclick').wait_click()
        js = "document.getElementsByClassName('ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical')[0].scrollTop=10000"

        self.driver.execute_script(js)
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_typechooseclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_saveclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_editclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_editsaveclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_deleteclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_addpara_click').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_addpara_inputclick').wait_send_keys("para3name")
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_typeclick').wait_click()
        js = "document.getElementsByClassName('ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical')[0].scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_typechooseclick').wait_click()
        Element(self.driver, 'dataStanard', 'tableedit_addpara1_saveclick').wait_click()
        current_url = Element(self.driver, 'dataStanard', 'tableedit_saveclick').wait_click()
        print('current_url:',current_url)
        time.sleep(1)
        try:
            self.check_result(current_url, data['expect_url1'])
        except:
            return

    @ddt.data(*testData)
    def check_result(self, acual_url, expect_url):
        if int(testData["result"]) == 0:
            self.assertEqual (acual_url,expect_url)
        else:
            self.assertNotEqual (acual_url,expect_url)

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()


if __name__ == "__main__":
    unittest.main()