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

sheetName = 'roleLook'
date = time.strftime('%Y%m%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()

@ddt.ddt
class RoleLook(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_RoleLook(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'systemManager','systemManager_click').wait_click()
        Element(self.driver,'systemManager','rolemanager_click').wait_click()
        time.sleep(2)
        for i in range(1,7):
            pathvalue = self.driver.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div[2]/div/div/div/div/div/table/tbody/tr[{}]/td[5]/span/a[1]'.format(i))

            print('pathvalue:',pathvalue)
            #点击查看按钮
            ActionChains(self.driver).move_to_element(pathvalue).click(pathvalue).perform()
            time.sleep(1)
            #取消查看
            Element(self.driver,'systemManager','rolemanager_cancelclick').wait_click()
            time.sleep(1)




    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()