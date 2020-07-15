#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/7/14 15:07 
# @name: runSet
# @author：menghuan.wmc
import os,sys
proDir = os.path.split(os.path.dirname(__file__))[0]


import unittest
filepath = ''

def set_case_list():
    caseList = []
    caseListPath = os.path.join(proDir,'caseList.txt')
    fb = open(caseListPath)
    for case in fb.readlines():
        data = str(case)
        if data != ""and not data.startswith('#'):
            caseList.append(data.replace("\n",""))
    fb.close()
    return caseList

def set_suite():
    global filepath
    suite_list = unittest.TestSuite()
    suite_module = []
    case_list = set_case_list()
    for case in case_list:
        name = str(case).split('/')[-1]
        module = str(case).split('/')[0]
        filepath = os.path.join(proDir,'case',module)
        # print('filepath:',filepath)
        discover = unittest.defaultTestLoader.discover(filepath,pattern=name +'.py',top_level_dir=filepath)
        suite_module.append(discover)
        # print(suite_module)

    if len(suite_module)>0:
        for case in suite_module:
            for name in case:
                # print('name:',name)
                suite_list.addTests(name)
    else:
        return None
    return suite_list

if __name__=="__main__":
    set_suite()






