#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2020/6/29 13:40 
# @name: element
# @author：menghuan.wmc
from selenium import webdriver
import sys,os,time
from xml.etree import ElementTree as ETree
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
path = os.path.split(os.path.dirname(__file__))[0]



activity = {}
def set_xml():
    """
    get element
    :return:
    """
    # web = runSet.get_web()
    # site = runSet.get_site()
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



def get_el_dict(activity_name, element):

    set_xml()
    #print(activity)
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

    def wait_element(self,wait_time):
        time.sleep(wait_time)
        if self.is_exist():
            return True
        else:
            return False

    def get_element(self):

        try:
            if self.pathType == "XPATH":
                element = self.driver.find_element_by_xpath(self.pathValue)

                return element
        except NoSuchElementException:
            return None
    def click(self):
        element = self.get_element()
        time.sleep(1)
        if element:
            element.click()
        self.driver.implicitly_wait(1)
        return self.driver.current_url
    def send_keys(self,key):
        element = self.get_element()
        if element:
            element.send_keys(key)
    def clear(self):
        element = self.get_element()
        if element:
            element.clear()

if __name__=="__main__":

    t = Element("project","createProject_click").get_element()












#
#
#
