#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 13:40
# @name: element
# @author：menghuan.wmc

import os,time
from xml.etree import ElementTree as ETree
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



path = os.path.split(os.path.dirname(__file__))[0]
activity = {}

def set_xml():
    """
    get element
    :return:
    """

    if len(activity) == 0:
        file_path = os.path.join(path, 'file', 'element.xml')
        tree = ETree.parse(file_path)
        for a in tree.findall('activity'):
            activity_name = a.get('name')

            element = {}
            for e in a.getchildren():
                element_name = e.get('id')

                element_child = {}
                for t in e.getchildren():
                    element_child[t.tag] = t.text
                element[element_name] = element_child
            activity[activity_name] = element
        return activity



def get_el_dict(activity_name, element):

    set_xml()
    element_dict = activity.get(activity_name).get(element)
    return element_dict



class Element():
    def __init__(self,driver,activity_name,element_name):
        self.driver = driver
        self.activity = activity_name
        self.element = element_name
        element_dict = get_el_dict(self.activity,self.element)
        self.pathType = element_dict.get('pathType')
        self.pathValue = element_dict.get('pathValue')


    def is_exist(self):

        try:
            if self.pathType =='XPATH':
                self.driver.find_element_by_xpath(self.pathValue)
                return True
        except NoSuchElementException:
            return False

    # 等待输入
    def wait_send_keys(self,key):
        element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,str(self.pathValue))))
        try:

            if element:
                element.send_keys(key)
        except (NoSuchElementException,TimeoutException)as e:
            raise e

    # 等待点击
    def wait_click(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, str(self.pathValue))))
        try:

            if element:
                element.click()
            return self.driver.current_url
        except (NoSuchElementException, TimeoutException)as e:
            raise e

    #等待元素消失
    def wait_not_click(self):
        element = WebDriverWait(self.driver, 20).until_not(EC.element_to_be_clickable((By.XPATH, str(self.pathValue))))
        return element


    #模拟键盘正常点击
    def click(self):
        element = self.get_element()
        if element:
            element.click()
    #模拟键盘操作
    def send_keys(self,*key):

        element = self.get_element()
        if element:
            element.send_keys(key)

    def clear(self):
        element = self.get_element()
        if element:
            element.clear()

    def wait_element(self, wait_time):
        """
        wait element appear in time
        :param wait_time: wait time
        :return: true or false
        """
        time.sleep(wait_time)
        if self.is_exist():
            return True
        else:
            return False

    def get_element(self):
        """
        get element
        :return: element
        """
        try:
            if self.pathType == 'XPATH':
                element = self.driver.find_element_by_xpath(self.pathValue)
                return element

        except NoSuchElementException:
            return None
    def get_text_value(self):
        element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,str(self.pathValue))))
        value = ''
        print('element',element)
        if element:
            value = element.text
        return str(value)
    def get_element_list(self):
        """
        get element list
        :return: element list
        """
        try:
            if self.pathType == 'ID':
                element_list = self.driver.find_element_by_id(self.pathValue)
                return element_list
            if self.pathType == 'XPATH':
                print(self.pathValue)
                element_list = self.driver.find_elements_by_xpath(self.pathValue)
                return element_list
            if self.pathType == 'CLASSNAME':
                element_list = self.driver.find_element_by_class_name(self.pathValue)
                return element_list
            if self.pathType == 'NAME':
                element_list = self.driver.find_element_by_name(self.pathValue)
                return element_list
            if self.pathType == 'SELECTOR':
                element_list = self.driver.find_element_by_css_selector(self.pathValue)
                return element_list
        except NoSuchElementException:
            return None

    #动态获取元素属性值
    def get_attribute(self,property):
        element = self.get_element()
        if element:
            time.sleep(2)
            value = element.get_attribute(property)
        return str(value)
    def get_attribute2(self):
        element = self.get_element()
        if element:
            time.sleep(1)
            value = element.get_attribute('textContent')
        return str(value)
    #判断元素是否可点击，一般用于查看按钮是否处于置灰状态
    def is_enabled(self):
        element = self.get_element()
        if element:
            element.is_enabled()
            return True
        else:
            return False
        # return element.is_enabled()
    def context_click(self):
        element = self.get_element()
        if element:
            element.context_click()



