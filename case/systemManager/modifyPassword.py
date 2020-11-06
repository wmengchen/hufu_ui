#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/11/4 16:35 
# @name: modifyPassword
# @author：menghuan.wmc

import ddt,unittest,sys,os,re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from comm.element import get_el_dict

sheetName = 'modifyPassword'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()
for item in testData:
     username = item['username']
     password = item['password']

@ddt.ddt
class ModifyPassword(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_ModifyPassword(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','usermanager_click').wait_click()
        Element(self.driver, 'systemManager', 'account_click').wait_send_keys(data["username2"])
        Element(self.driver,'systemManager','account_click_find').wait_click()
        Element(self.driver,'systemManager','modifyPassword_click').wait_click()
        Element(self.driver,'systemManager','modifyPassword_click')
        Element(self.driver, 'systemManager', 'oldPassword_click').wait_send_keys(data['password2'])
        Element(self.driver, 'systemManager', 'newPassword_click').wait_send_keys(data['confirmPassword'])
        Element(self.driver,'systemManager', 'modifyPassword_cancelclick').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'account_click').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'account_click').send_keys(Keys.DELETE)
        time.sleep(1)
        Element(self.driver, 'systemManager', 'account_click').wait_send_keys(data["username"])
        Element(self.driver, 'systemManager', 'account_click_find').wait_click()
        Element(self.driver, 'systemManager', 'modifyPassword_click').wait_click()
        Element(self.driver, 'systemManager', 'oldPassword_click').wait_send_keys(data['password'])
        Element(self.driver, 'systemManager', 'newPassword_click').wait_send_keys(data['confirmPassword'])
        Element(self.driver, 'systemManager', 'modifyPassword_okclick').wait_click()
        try:
            Element(self.driver, 'systemManager', 'modifyPassword_okclick').wait_not_click()
        except:
            Element(self.driver, 'systemManager', 'cancel_click').wait_click()

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()