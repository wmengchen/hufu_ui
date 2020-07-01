#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 10:54 
# @name: setting
# @author：menghuan.wmc
import sys,os

Base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Base_dir)

#配置文件
Test_config = os.path.join(Base_dir,'database','config.ini')
#测试用例文件
Test_case = os.path.join(Base_dir,'database','虎符测试用例.xlsx')
#测试用例执行文件
Test_case_execute = os.path.join(Base_dir,'case')

