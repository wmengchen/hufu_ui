#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/28 16:02 
# @name: login
# @author：menghuan.wmc
from selenium import webdriver
from time import sleep
import sys,os
import configparser as cparser
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from comm.sql import Dbconnect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#读取配置文件
cf = cparser.ConfigParser()
cf.read(setting.Test_config,encoding='utf-8')
test_url = cf .get('test_env','url')
test_user = cf.get('test_admin','username')
test_pwd = cf.get('test_admin','password')


account = {
    "test_admin":{
        "username":"menghuan",
        "password":"mh1234d"
    },
    "test_safeadmin":{
        "username":"wmenghuan7",
        "password":"mh1234"
    },
    "test_auditadmin":{
        "username":"wmenghuan8",
        "passworf":"mh1234"
    }

}
class Login():

    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self):

        self.browser.get(test_url)
        self.browser.maximize_window()
        sleep(1)

        self.browser.find_element_by_xpath("//input[@id='username']").send_keys(test_user)
        sleep(1)
        self.browser.find_element_by_xpath("//input[@id='password']").send_keys(test_pwd)
        sleep(1)
        self.browser.find_element_by_xpath("//input[@placeholder='验证码']").send_keys('1111')
        sleep(1)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        # browser.find_element_by_xpath('').click()
        # browser.find_element_by_xpath('//button[@class = "ant-btn ant-btn-primary"]').click()
        # browser.find_element_by_xpath('//input[@placeholder="请输入项目名称"]').send_keys('ceshixuyao1112311')
        # browser.find_element_by_xpath('//textarea[@placeholder="请输入描述"]').send_keys('nihao')
        # browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        # sleep(8)
        # nihao = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,'/div/div/div/span')))
        # print(nihao)
        # sleep(1)
if __name__=="__main__":
    l= Login()
    l.login()