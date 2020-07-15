# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# # @date: 2020/4/14 11:27
# # @name: setting
# # @author：menghuan.wmc
#
#
import os, sys,time
sys.path.append(os.path.dirname(__file__))
print('os:',os.path.dirname(__file__))

from config import setting
from package.HTMLTestRunner import HTMLTestRunner
from comm.runSet import set_suite
import HTMLTestRunner_PY3


result_path = setting.Test_report


def run_case(result_path=setting.Test_report):
    """执行所有的测试用例"""

    now = time.strftime("%Y-%m-%d %H_%M")
    filename = result_path + '/' + now + ' result.html'
    fp = open(filename,'wb')

    suite = set_suite()
    print('suite:',suite)
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title='虎符自动化测试报告', description='测试用例结果')

    runner.run(suite)
    fp.close()


if __name__ == "__main__":
    run_case()
