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
from .saferapprove import Saferapprove
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')


sheetName = 'safemangeropenoff'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()



@ddt.ddt
class Safemangeropenoff(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_Safemangeropenoff(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','safemanager_click').wait_click()
        print('三员管理的开启状态是：',Element(self.driver, 'systemManager', 'safemanager_openclick').get_attribute('aria-checked'))
        #判断是否开启三员管理，若未开启则开启
        if Element(self.driver, 'systemManager', 'safemanager_openclick').get_attribute('aria-checked') == 'false':


            Element(self.driver, 'systemManager', 'safemanager_openclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_saferclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_saferselect').wait_click()
            time.sleep(1)
            Element(self.driver, 'systemManager', 'safemanager_auditerclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_auditerselect').wait_click()
            time.sleep(2)
            Element(self.driver, 'systemManager', 'safemanager_useraddclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_usereditclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_modifypasswordclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_roleeditclick').wait_click()
            Element(self.driver, 'systemManager', 'safemanager_saveclick').wait_click()
            time.sleep(1)
            #提交关闭三员管理
            Element(self.driver, 'systemManager', 'safemanager_openclick').wait_click()
            time.sleep(1)
            #安全管理员驳回关闭三员管理
            self.Saferapprove().test_Saferapprove_reject()
            time.sleep()

        else:
            Element(self.driver, 'systemManager', 'safemanager_openclick').wait_click()
            time.sleep(1)
            self.Saferapprove().test_Saferapprove_pass()


    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()