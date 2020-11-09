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
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_safeadmin','username')
password = cf.get('test_safeadmin','password')

sheetName = 'saferapprove'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()


class safer_approve():
    def __init__(self):
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
    def Safer_reject(self):

        Element(self.driver, 'systemManager', 'systemManager_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'saferapprove_approveclick').wait_click()
        Element(self.driver, 'systemManager', 'saferapprove_contextclick').wait_send_keys('test')
        Element(self.driver, 'systemManager', 'saferapprove_rejectclick').wait_click()
        time.sleep(1)
        self.login.logout()
    def Safer_pass(self):
        Element(self.driver, 'systemManager', 'systemManager_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'systemManager', 'saferapprove_approveclick').wait_click()
        Element(self.driver, 'systemManager', 'saferapprove_contextclick').wait_send_keys('test')
        Element(self.driver, 'systemManager', 'saferapprove_passclick').wait_click()
        time.sleep(1)
        self.login.logout()

#
# @ddt.ddt
# class Saferapprove(unittest.TestCase):
#
#     def setUp(self):
#         print('--------测试开始--------')
#         self.login = login.Login()
#         self.login.login(username, password)
#         self.driver = self.login.browser
#         pass
#
#     @ddt.data(*testData)
#
#     def test_Saferapprove_pass(self,data):
#         print('---------{}---------'.format(data['case_name']))
#
#         Element(self.driver, 'systemManager', 'systemManager_click').wait_click()
#         time.sleep(1)
#         Element(self.driver, 'systemManager', 'saferapprove_approveclick').wait_click()
#         Element(self.driver, 'systemManager', 'saferapprove_contextclick').wait_send_keys(data["approve_context"])
#         Element(self.driver, 'systemManager', 'saferapprove_passclick').wait_click()
#         time.sleep(1)
#
#     def test_Saferapprove_reject(self, data):
#         print('---------{}---------'.format(data['case_name']))
#
#         Element(self.driver, 'systemManager', 'systemManager_click').wait_click()
#         time.sleep(1)
#         Element(self.driver, 'systemManager', 'saferapprove_approveclick').wait_click()
#         Element(self.driver, 'systemManager', 'saferapprove_contextclick').wait_send_keys(data["approve_context"])
#         Element(self.driver, 'systemManager', 'saferapprove_rejectclick').wait_click()
#         time.sleep(1)
#
#
#
#
#     def tearDown(self):
#         print('--------测试结束--------')
#         self.login.logout()

if __name__=="__main__":
    test = safer_approve()
    test.Safer_pass()