# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/4/14 11:27
# @name: setting
# @author：menghuan.wmc


import os, sys

sys.path.append(os.path.dirname(__file__))
pro_path = os.path.dirname(__file__)
import time
import unittest
from config import setting
from package.HTMLTestRunner import HTMLTestRunner




test_path = setting.Test_case_execute
second_dir_path = os.listdir(test_path)
print('second_dir_path:',second_dir_path)
result_path = setting.Test_report


def run_case(result_path=setting.Test_report):
    """执行所有的测试用例"""

    now = time.strftime("%Y-%m-%d %H_%M")
    filename = result_path + '/' + now + ' result.html'
    fp = open(filename, 'wb')
    #加入case列表
    dir1 = "case/project"
    dir2 = "case/dataSource"
    test_dirs = list()
    test_dirs.append(dir1)
    test_dirs.append(dir2)



    suite = unittest.TestSuite()
    for item in test_dirs:
        discover = unittest.defaultTestLoader.discover(start_dir=item,pattern='*test.py',top_level_dir=None)
        for case1 in discover:
            for case in case1:
                suite.addTests(case)

        runner = HTMLTestRunner(stream=fp, title='虎符接口自动化测试报告',
                                description='环境：windows 10 浏览器：chrome',
                                tester='menghuan')

        runner.run(suite)

    # case_path = os.path.join(pro_path, 'case')
    # print('case_path:',case_path)
    # list_case = ['project','dataSource']
    # suite = unittest.TestSuite()
    #
    # for i in range(len(list_case)):
    #
    #     discover = unittest.defaultTestLoader.discover(case_path+"/" +list_case[i], pattern='*_test.py', top_level_dir=None)



if __name__ == "__main__":
    run_case()







