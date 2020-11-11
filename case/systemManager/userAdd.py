#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/24 10:28 
# @name: userAdd
# @author：menghuan.wmc

import ddt,unittest,sys,os,re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
import time
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')
sheetName = 'userAdd'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()



@ddt.ddt
class UserAdd(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_UserAdd(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','usermanager_click').wait_click()
        time.sleep(1)
        Element(self.driver,'systemManager','userAdd_click').wait_click()
        time.sleep(2)
        Element(self.driver,'systemManager','userName_click').wait_send_keys(date+data["username2"])
        time.sleep(1)
        Element(self.driver,'systemManager','password_click').wait_send_keys(data["password2"])
        time.sleep(1)
        Element(self.driver,'systemManager','confirmPassword_click').wait_send_keys(data["confirmPassword"])
        time.sleep(1)
        Element(self.driver,'systemManager','email_click').wait_send_keys(date+data["email"])
        time.sleep(1)

        Element(self.driver,'systemManager','phone_click').wait_send_keys(str(int(data["phone"]))+date)
        time.sleep(1)
        Element(self.driver, 'systemManager','name_click').wait_send_keys(data["name"])
        time.sleep(1)
        Element(self.driver,'systemManager','department_click').wait_send_keys(data["partment"])
        time.sleep(1)
        Element(self.driver,'systemManager','position_click').wait_send_keys(data["position"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'open_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'open_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager','cancel_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'userAdd_click').wait_click()
        Element(self.driver, 'systemManager', 'userName_click').wait_send_keys(date + data["username2"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'password_click').wait_send_keys(data["password2"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'confirmPassword_click').wait_send_keys(data["confirmPassword"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'email_click').wait_send_keys(date+data["email"])
        time.sleep(1)

        Element(self.driver, 'systemManager', 'phone_click').wait_send_keys(str(int(data["phone"]))+date)
        time.sleep(1)
        Element(self.driver, 'systemManager', 'name_click').wait_send_keys(data["name"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'department_click').wait_send_keys(data["partment"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'position_click').wait_send_keys(data["position"])
        time.sleep(1)
        Element(self.driver, 'systemManager', 'open_click').wait_click()
        Element(self.driver, 'systemManager','save_click').wait_click()
        try:
            Element(self.driver, 'systemManager', 'save_click').wait_not_click()
        except:
            Element(self.driver, 'systemManager', 'cancel_click').wait_click()

        time.sleep(1)
        Element(self.driver,'systemManager','account_click').wait_send_keys(date+data["username2"])
        time.sleep(1)
        content = Element(self.driver,'systemManager','total_click').get_text_value()
        print('content:',content)

        self.check_result(content)

    def check_result(self,content):
        number = re.findall(r"\d+\.?\d*", content)
        s = number[0]
        assert int(s)==1




    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()