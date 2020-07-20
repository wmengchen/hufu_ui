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
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from comm.element import Element
from selenium.webdriver.common.keys import Keys
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
        k = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]')))
        # print('k',k)
        k.click()




        #单元测试验证具体页面
        # sleep(1)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div[1]/span/input').send_keys('2020-07-20_wmc_edit')
        # sleep(1)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div[1]/span/input').send_keys(Keys.ENTER)
        # sleep(2)
        # self.browser.find_element_by_xpath('//p[@class="item-title"]').click()
        # sleep(1)
        # self.browser.find_element_by_xpath('//li/a[text()="数据资产"]').click()
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/p/button').click()
        # sleep(2)
        # js = "document.getElementsByClassName('add-dataSourde')[0].scrollTop=1000"
        # self.browser.execute_script(js)
        #
        # sleep(10)


    def logout(self):
        self.browser.close()

if __name__=="__main__":
    l= Login()
    l.login()