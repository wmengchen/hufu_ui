#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 11:16 
# @name: createProject
# @author：menghuan.wmc
import ddt,unittest,sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from comm.element import  Element
from comm.readExcel import ReadExcel
from comm.login import Login
from config import setting
from comm.sql import Dbconnect
import time

sheetName = 'project'

testData = ReadExcel(setting.Test_case,sheetName).read_data()
print(testData)
time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

@ddt.ddt
class Project(unittest.TestCase):


    def setUp(self):
        print('--------测试开始--------')
        self.login = Login()
        Login().login()
        self.browser = self.login.browser
        pass

    @ddt.data(*testData)
    def test_createProject(self,data):

        # 获取ID的数值，截取结尾只获取数字
        # row_num = (data['case_name']).split("_")[0]
        # print(data['project_name'])
        print('---------开始执行测试用例:{}---------'.format(data['case_name']))

        Element('project','createProject_click').click()
        Element('project','Projectname_click').send_keys( time +data["project_name"])
        time.sleep(200)
        Element('project','Projectdesc_click').send_keys(data["project_desc"])
        # Element(self.browser,'project','Projectcancel_click').click()
        # time.sleep(1)
        # Element(self.browser, 'project', 'createProject_click').click()
        # Element(self.browser, 'project', 'Projectname_click').send_keys(time + data["project_name"])
        # Element(self.browser, 'project', 'Projectdesc_click').send_keys(data["project_desc"])
        # Element(self.browser,'project','Projectok_click').click()
        # self.assertEqual(Dbconnect.sql_ProjectInfo())

    #
    # def test_editProject(self,data):
    #
    #     Element(self)

if __name__=="__main__":
    unittest.main()











