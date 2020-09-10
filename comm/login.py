#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/28 16:02 
# @name: login
# @author：menghuan.wmc
from selenium import webdriver
from time import sleep
import sys,os,random
import configparser as cparser
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from comm.sql import Dbconnect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from comm.element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
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
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()

        sleep(3)




        #单元测试验证具体页面
        # sleep(1)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div[1]/span/input').send_keys('2020-09-02_自动化测试勿操作！')
        # sleep(2)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div[1]/span/input').send_keys(Keys.ENTER)
        # sleep(2)
        # self.browser.find_element_by_xpath('//p[@class="item-title"]').click()
        # sleep(2)
        #
        # self.browser.find_element_by_xpath("//li/a[text()='数据标准']").click()
        #
        # self.browser.find_element_by_xpath("//span[text()='模型设计']").click()
        # # WebDriverWait.until(self.browser,3).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='模型设计']")))
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div[2]/div[2]/button").click()
        # sleep(1)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div/div/div[2]/div/ul[1]/li[1]/div/div/p[2]/div/div/div/div').click()
        # sleep(1)
        # self.browser.find_element_by_xpath("//li[text()='ads']").click()
        # sleep(1)
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul[1]/li[1]/div/div[2]/p[2]/div").click()
        # sleep(1)
        # self.browser.find_element_by_xpath("//li[text()='ai']").click()
        # sleep(1)
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul[1]/li[1]/div/div[3]/p[2]/input").send_keys('niha')
        # self.browser.find_element_by_xpath(
        #     "//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul[1]/li[3]/textarea").send_keys(
        #     'niha')
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[3]/button[2]").click()
        # # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul/li/div/div[2]/span").click()
        # # self.browser.find_element_by_xpath("//div[@class='ant-select-selection__rendered']").click()
        # # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul/li/div/div[1]/div/div/div/div/div/table/tbody/tr/td[1]/div/div/div/div/div[3]/div/input").send_keys("nihao")
        # # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul/li/div/div[1]/div/div/div/div/div/table/tbody/tr/td[2]/div/div/div/div/div").click()
        # # self.browser.find_element_by_xpath("//li[text()='int']").click()
        # # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul/li/div/div[1]/div/div/div/div/div/table/tbody/tr/td[4]/div/span").click()
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[3]/button[3]").click()
        # sleep(5)
        # context = self.browser.find_element_by_xpath("/html/body/div[2]/div/span/div/div/div/span").get_attribute("textContent")
        # print("context的内容是：",context)



        # sleep(1)
        # self.browser.find_element_by_xpath("//*[@id='container']/section/section/section/main/div/div/div/div[2]/div/ul[1]/li[3]/textarea").send_keys('1212121212222222222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112121212122222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div/div/div[3]/button[2]').click()
        # sleep(5)
        # self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div/div/div[3]/button[2]').click()
        # sleep(1)
        # vlues = self.browser.find_element_by_xpath('//*[@id="container"]/section/section/section/main/div/div/div/div[3]/button[2]').get_attribute('ant-click-animating-without-extra-node')
        # print('vlues的值是：',vlues)

        # url= WebDriverWait(self.browser, 20).until_not(EC.visibility_of_element_located((By.XPATH, '/*[@id="container"]/section/section/section/main/div/div/div/div[3]/button[2]')))

        # s = random.randrange(1,6)
        # print('s的值是：',s)
        # if s==1:
        #     self.browser.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[1]").click()
        # elif s==2:
        #     self.browser.find_element_by_xpath(
        #         "//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[2]").click()
        # elif s == 3:
        #     self.browser.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[3]").click()
        # elif s == 4:
        #     self.browser.find_element_by_xpath(
        #         "//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[4]").click()
        # elif s == 5:
        #     self.browser.find_element_by_xpath(
        #         "//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[5]").click()
        #
        # sleep(5)
        # sleep(1)
        # self.browser.find_element_by_xpath('//li/a[text()="数据资产"]').click()
        #
        # self.browser.find_element_by_xpath('//div[@class="content-header"]/input').send_keys("default")
        # sleep(4)
        # user = Element(self.browser, 'dataAssert', 'dataSourcedefaultname_click').get_attribute()
        # sleep(5)
        # print('s的值是：',user)
        # Element(self.browser, 'dataAssert', 'dataSourceadd_click').wait_click()
        # Element(self.browser, 'dataAssert', 'dataSourceAddhive_click').wait_click()
        # sleep(1)
        # Element(self.browser, 'dataAssert', 'dataSourceadd_nextclick').wait_click()
        # sleep(1)
        # Element(self.browser, 'dataAssert', 'dataSourceAddhivepre_click').wait_click()
        # sleep(1)

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