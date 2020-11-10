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
from .saferapprove import safer_approve
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')


sheetName = 'accountRegular'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()



@ddt.ddt
class AccountRegular(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_AccountRegular(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','accountRegular_click').wait_click()
        Element(self.driver,'systemManager','accountRegular_editclick').wait_click()
        Element(self.driver, 'systemManager', 'accountRegular_Structuredstorageclick').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'accountRegular_Structuredstorageclick').send_keys(Keys.DELETE)
        Element(self.driver, 'systemManager','accountRegular_Structuredstorageclick').wait_send_keys(int(data["Structuredstorage"]))
        Element(self.driver, 'systemManager', 'accountRegular_notStructuredstorageclick').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'accountRegular_notStructuredstorageclick').send_keys(Keys.DELETE)
        Element(self.driver, 'systemManager', 'accountRegular_notStructuredstorageclick').wait_send_keys(int(data["NotStructuredstorage"]))
        Element(self.driver, 'systemManager', 'accountRegular_cpuclick').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'accountRegular_cpuclick').send_keys(Keys.DELETE)
        Element(self.driver, 'systemManager', 'accountRegular_cpuclick').wait_send_keys(int(data["Cpu"]))
        Element(self.driver, 'systemManager', 'accountRegular_Gpuclick').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'accountRegular_Gpuclick').send_keys(Keys.DELETE)
        Element(self.driver, 'systemManager', 'accountRegular_Gpuclick').wait_send_keys(int(data["Gpu"]))
        Element(self.driver, 'systemManager', 'accountRegular_memoryclick').send_keys(Keys.CONTROL+'a')
        Element(self.driver, 'systemManager', 'accountRegular_memoryclick').send_keys(Keys.DELETE)
        Element(self.driver,'systemManager','accountRegular_memoryclick').wait_send_keys(int(data["Memory"]))
        time.sleep(1)
        Element(self.driver,'systemManager','accountRegular_saveclick').wait_click()
        if Element(self.driver,'systemManager','accountRegular_saveclick').get_attribute("span") =='编辑':
            context = Element(self.driver,'systemManager','accountRegular_savesuccessclick').get_attribute2()
            print('提交的内容：',context)
            self.assertEqual(context,'修改成功')
        else:
            pass

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()