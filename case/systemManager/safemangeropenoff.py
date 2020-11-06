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



sheetName = 'safemangeropenoff'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()
for item in testData:
     username = item['username']
     password = item['password']


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
            Element(self.driver, 'systemManager', 'safemanager_openclick').wait_click()
            time.sleep(1)
            Saferapprove().test_Saferapprove()
            # Saferapprove().test_Saferapprove()
            # self.Saferapprove.test_Saferapprove()
        else:
            print('test')



    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()