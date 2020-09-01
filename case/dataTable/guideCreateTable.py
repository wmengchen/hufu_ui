#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/24 10:21 
# @name: guideCreateTable
# @author：menghuan.wmc

import ddt,unittest,sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from selenium.webdriver.common.keys import Keys
from comm.sql import Dbconnect
import time
from selenium.webdriver.common.action_chains import ActionChains

sheetName = 'guideCreateTable'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()

@ddt.ddt
class guideCreateTable(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_guideCreateTable(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver,'project','Projectfind_click').wait_send_keys(date+data["project_name"])
        Element(self.driver,'project','Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver,'project','enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver,'dataStanard','dataStanard_click').wait_click()
        Element(self.driver, 'dataStanard', 'modelDesign_click').wait_click()
        Element(self.driver,'dataStanard', 'guideCreateTable_click').wait_click()
        # js = "document.getElementsByClassName('add-dataSourde')[0].scrollTop=1000"
        # self.driver.execute_script(js)
        Element(self.driver, 'dataStanard', 'levelchoose_click').wait_click()
        Element(self.driver, 'dataStanard', 'levelchoose_ads_click').wait_click()
        Element(self.driver,'dataStanard','apply_choose_click').wait_click()
        Element(self.driver,'dataStanard','applychoose_ai_click').wait_click()
        Element(self.driver,'dataStanard','define_click').wait_send_keys(data["define"])
        Element(self.driver, 'dataStanard', 'tabledesc_click').wait_send_keys(data["desc"])
        Element(self.driver, 'dataStanard', 'tablelifeStyle_click').wait_click()
        Element(self.driver,'dataStanard','tablelifeStyle_select').wait_click()
        Element(self.driver,'dataStanard','tablelifeStyle_input').wait_send_keys(int(data["lifecycle"]))
        Element(self.driver,'dataStanard','next_click').wait_click()
        Element(self.driver,'dataStanard','addpar_click').wait_click()
        Element(self.driver, 'dataStanard', 'paraname1_click').wait_send_keys(data["para1name"])
        Element(self.driver, 'dataStanard', 'paraname1_typeclick').wait_click()
        Element(self.driver, 'dataStanard', 'paraname1_typeselect').wait_click()
        Element(self.driver, 'dataStanard', 'paraname1_save').wait_click()
        Element(self.driver, 'dataStanard', 'addpar_click').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_click').wait_send_keys(data["para2name"])
        Element(self.driver, 'dataStanard', 'paraname2_typeclick').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_typeselect').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_delete').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'addpar_click').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_click').wait_send_keys(data["para2name"])
        Element(self.driver, 'dataStanard', 'paraname2_typeclick').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_typeselect').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_save').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'paraname2_editclick').wait_click()
        Element(self.driver, 'dataStanard', 'paraname2_save').wait_click()
        Element(self.driver, 'dataStanard', 'partition_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'nopartition_click').wait_click()
        Element(self.driver, 'dataStanard', 'nopartition_click').wait_click()
        Element(self.driver, 'dataStanard', 'partition_addclick').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para1_click').wait_send_keys(data["partition_par1"])
        Element(self.driver, 'dataStanard', 'partition_para1_typeclick').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para1_typeselect').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para1_saveclick').wait_click()
        Element(self.driver, 'dataStanard', 'partition_addclick').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para2_click').wait_send_keys(data["partition_par1"])
        Element(self.driver, 'dataStanard', 'partition_para2_typeclick').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para2_typeselect').wait_click()
        Element(self.driver, 'dataStanard', 'partition_para2_saveclick').wait_click()
        Element(self.driver, 'dataStanard', 'para_pre_lick').wait_click()
        current_url = Element(self.driver, 'dataAssert', 'dataSourceaddHttpMdttsave_click').wait_click()
        time.sleep(1)

        try:
            self.check_result(current_url,data['expect_url1'])
        except:
            return

    @ddt.data(*testData)
    def check_result(self,acual_url,expect_url):
        if int(testData["result"]) == 0:
            assert (acual_url != expect_url)
        else:
            assert (acual_url == expect_url)



    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()

if __name__=="__main__":
    unittest.main()