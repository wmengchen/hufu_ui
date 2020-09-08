# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/24 10:21
# @name: guideCreateTable
# @author：menghuan.wmc

import ddt, unittest, sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import Element
from comm.readExcel import ReadExcel
from comm import login
from config import setting
from selenium.webdriver.common.keys import Keys



sheetName = 'guideCreateTable_dws'
date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
testData = ReadExcel(setting.Test_case, sheetName).read_data()


@ddt.ddt
class guideCreateTable_dws(unittest.TestCase):

    def setUp(self):
        print('--------测试开始--------')
        self.login = login.Login()
        self.login.login()
        self.driver = self.login.browser
        pass

    @ddt.data(*testData)
    def test_guideCreateTable_dws(self, data):

        print('---------{}---------'.format(data['case_name']))

        Element(self.driver, 'project', 'Projectfind_click').wait_send_keys(date + data["project_name"])
        Element(self.driver, 'project', 'Projectfind_click').send_keys(Keys.ENTER)
        time.sleep(1)
        Element(self.driver, 'project', 'enterProject_click').wait_click()
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'dataStanard_click').wait_click()
        Element(self.driver, 'dataStanard', 'modelDesign_click').wait_click()
        Element(self.driver, 'dataStanard', 'guideCreateTable_click').wait_click()
        Element(self.driver, 'dataStanard', 'levelchoose_click').wait_click()
        Element(self.driver, 'dataStanard', 'dws_chooseclick').wait_click()
        Element(self.driver, 'dataStanard', 'apply_choose_click').wait_click()
        Element(self.driver, 'dataStanard', 'dwd__prdclick').wait_click()
        Element(self.driver, 'dataStanard', 'dwd__apclick').wait_click()
        Element(self.driver,'dataStanard','dwd__apchooseclick').wait_click()
        Element(self.driver,'dataStanard','dwd__increamclick').wait_click()
        Element(self.driver, 'dataStanard', 'dwd__increamchoose_click').wait_click()
        Element(self.driver, 'dataStanard', 'dwd__define_click').wait_send_keys(data["define"])
        Element(self.driver, 'dataStanard', 'dwd__flency_click').wait_click()
        Element(self.driver, 'dataStanard', 'dwd__flency_chooseclick').wait_click()

        Element(self.driver, 'dataStanard', 'tabledesc_click').wait_send_keys(data["desc"])
        Element(self.driver, 'dataStanard', 'tabledesc_info').wait_click()
        time.sleep(1)
        value = Element(self.driver, 'dataStanard', 'tabledesc_info').get_attribute(data["property"])
        print('value的值是：', value)
        Element(self.driver, 'dataStanard', 'tablelifeStyle_click').wait_click()
        Element(self.driver, 'dataStanard', 'tablelifeStyle_select').wait_click()
        Element(self.driver, 'dataStanard', 'tablelifeStyle_input').wait_send_keys(int(data["lifecycle"]))
        time.sleep(1)
        Element(self.driver, 'dataStanard', 'next_click').wait_click()
        if value == 'correct':
            Element(self.driver, 'dataStanard', 'addpar_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname1_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname1_inputclick').wait_send_keys(data["para1name"])
            Element(self.driver, 'dataStanard', 'paraname1_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname1_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'paraname1_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'para1desc_intputclick').wait_send_keys(data["para1desc"])
            Element(self.driver, 'dataStanard', 'paraname1_save').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'addpar_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_inputclick').wait_send_keys(data["para2name"])
            Element(self.driver, 'dataStanard', 'paraname2_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'para2desc_inputclick').wait_send_keys(data["para2desc"])
            Element(self.driver, 'dataStanard', 'paraname2_save').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'paraname2_delete').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'addpar_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_inputclick').wait_send_keys(data["para2name"])
            Element(self.driver, 'dataStanard', 'paraname2_click').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'para2desc_inputclick').wait_send_keys(data["para2desc"])
            Element(self.driver, 'dataStanard', 'paraname2_save').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'paraname2_editclick').wait_click()
            Element(self.driver, 'dataStanard', 'paraname2_save').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'partition_click').wait_click()
            Element(self.driver, 'dataStanard', 'nopartition_click').wait_click()
            Element(self.driver, 'dataStanard', 'partition_click').wait_click()
            Element(self.driver, 'dataStanard', 'partition_addclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1_click').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1_inputclick').wait_send_keys(data["partition_par1"])
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'partition_para1_inputclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1desc_inputclick').wait_send_keys(data["partition1_desc"])
            Element(self.driver, 'dataStanard', 'partition_para1desc_inputclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para1_saveclick').wait_click()
            #
            Element(self.driver, 'dataStanard', 'partition_addclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_click').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_inputclick').wait_send_keys(data["partition_par2"])
            time.sleep(2)
            Element(self.driver, 'dataStanard', 'partition_para2_inputclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_descClick').wait_send_keys(data["partition2_desc"])
            Element(self.driver, 'dataStanard', 'partition_para2_saveclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_editclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_saveclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_deleteclick').wait_click()
            # time.sleep(1)
            Element(self.driver, 'dataStanard', 'partition_addclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_click').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_inputclick').wait_send_keys(data["partition_par2"])
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'partition_para2_inputclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_typeclick').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_typeselect').wait_click()
            Element(self.driver, 'dataStanard', 'partition_para2_descClick').wait_send_keys(data["partition2_desc"])

            Element(self.driver, 'dataStanard', 'partition_para2_saveclick').wait_click()
            time.sleep(1)
            Element(self.driver, 'dataStanard', 'para_pre_lick').wait_click()
            Element(self.driver, 'dataStanard', 'next_click').wait_click()
            Element(self.driver, 'dataStanard', 'para_save_click').wait_click()
            Element(self.driver, 'dataStanard', 'para_save_click').wait_click()
            value2 = Element(self.driver, 'dataStanard', 'para_save_click').get_attribute(data["property2"])
            print('value2：', value2)
            try:
                self.check_result(value2)
            except:
                return
        else:
            pass
            #

    @ddt.data(testData)
    def check_result(self, value):
        if int(testData["result"]) == 0:
            self.assertEqual(value, testData["expect_result"])
        else:
            self.assertEqual(value, testData["expect_result"])

    def tearDown(self):
        print('--------测试结束--------')
        self.login.logout()


if __name__ == "__main__":
    unittest.main()