#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/24 17:44 
# @name: userEdit
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

sheetName = 'userEdit'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()
for item in testData:
     username = item['username']
     password = item['password']

@ddt.ddt
class UserEdit(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_UserEdit(self,data):

        print('---------{}---------'.format(data['case_name']))
        global s,str1

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','usermanager_click').wait_click()
        Element(self.driver, 'systemManager', 'account_click').wait_send_keys(date + data["username2"])
        time.sleep(1)
        Element(self.driver,'systemManager','usernamecheck_click').wait_click()
        Element(self.driver, 'systemManager',"usernamecheckcancel_click").wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager','usernameEdit_click').wait_click()
        Element(self.driver, 'systemManager','email_click').send_keys(Keys.CONTROL,'a')
        Element(self.driver, 'systemManager', 'email_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'email_click').wait_send_keys(date+data["email"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'phone_click').send_keys(Keys.CONTROL,'a')
        Element(self.driver, 'systemManager', 'phone_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'phone_click').wait_send_keys(str(int(data["phone"]))+date)
        time.sleep(1)
        Element(self.driver, 'systemManager', 'name_click').send_keys(Keys.CONTROL,'a')
        Element(self.driver, 'systemManager', 'name_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'name_click').wait_send_keys(data["name"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'usernameEditcancel_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'usernameEdit_click').wait_click()
        Element(self.driver, 'systemManager', 'email_click').send_keys(Keys.CONTROL, 'a')
        Element(self.driver, 'systemManager', 'email_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'email_click').wait_send_keys(date+data["email"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'phone_click').send_keys(Keys.CONTROL, 'a')
        Element(self.driver, 'systemManager', 'phone_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'phone_click').wait_send_keys(str(int(data["phone"]))+date)
        time.sleep(1)
        Element(self.driver, 'systemManager', 'name_click').send_keys(Keys.CONTROL, 'a')
        Element(self.driver, 'systemManager', 'name_click').send_keys(Keys.BACK_SPACE)
        Element(self.driver, 'systemManager', 'name_click').wait_send_keys(data["name"])
        time.sleep(1)
        Element(self.driver,'systemManager','usernameEditok_click').wait_click()
        time.sleep(1)
        Element(self.driver,'systemManager','usernameModifyPassword_click').wait_click()
        Element(self.driver,'systemManager','password_click').wait_send_keys(data["password2"])
        time.sleep(1)
        Element(self.driver,'systemManager','usernameModifyPasswordconfirm_click').wait_send_keys(data["confirmPassword"])
        time.sleep(1)
        Element(self.driver, 'systemManager','usernameModifyPasswordcancel_click').wait_click()
        Element(self.driver, 'systemManager', 'usernameModifyPasswordcancel_click').wait_not_click()
        Element(self.driver, 'systemManager', 'usernameModifyPassword_click').wait_click()
        Element(self.driver, 'systemManager', 'password_click').wait_send_keys(data["password"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'usernameModifyPasswordconfirm_click').wait_send_keys(data["confirmPassword"])
        time.sleep(1)
        Element(self.driver,'systemManager','usernameModifyPasswordok_click').wait_click()
        time.sleep(1)
        content = Element(self.driver, 'systemManager', 'total_click').get_text_value()

        self.check_result(content)


    def check_result(self,content):
        number = re.findall(r"\d+\.?\d*", content)
        s = number[0]
        assert  int(s)==1




    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()