#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/20 15:40 
# @name: opentsdb_publicNetAdd
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
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
username = cf.get('test_admin','username')
password = cf.get('test_admin','password')
sheetName = 'opentsdb_publicNetAdd'
date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
testData = ReadExcel(setting.Test_case,sheetName).read_data()


@ddt.ddt
class Opentsdb_publicNetAdd(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login(username, password)
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_opentsdb_publicNetAdd(self,data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver, 'project', 'Projectfind_click').wait_send_keys(date + data["project_name"])
        Element(self.driver, 'project', 'Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver, 'project', 'enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataAssert', 'dataAssert_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSource_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_click').wait_click()
        js = "document.getElementsByClassName('add-dataSourde')[0].scrollTop=1000"
        self.driver.execute_script(js)
        # time.sleep(2)
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdb_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpre_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpubliciptype_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpubliciptype_select').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbname_click').wait_send_keys(data["dataSource_name"] + date)
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbdesc_click').wait_send_keys(date + data["dataSouce_desc"])
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpublicipurl_click').wait_send_keys(data["url"])
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbconnect_click').wait_click()
        Element(self.driver,'dataAssert','dataSourceaddopentsdbparaAdd_click').wait_click()
        Element(self.driver,'dataAssert','dataSourceaddopentsdbpara1name_click').wait_send_keys(data["paraname1"])
        Element(self.driver, 'dataAssert','dataSourceaddopentsdbpara1type_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpara1type2_select').wait_click()
        Element(self.driver,'dataAssert','dataSourceaddopentsdbdelete_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbparaAdd_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpara1name_click').wait_send_keys(data["paraname1"])
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpara1type_click').wait_click()
        Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbpara1type2_select').wait_click()
        current_url = Element(self.driver, 'dataAssert', 'dataSourceaddopentsdbsave_click').wait_click()
        time.sleep(1)

        try:
            self.check_result(current_url, data['expect_url1'])
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