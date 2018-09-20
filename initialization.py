#!/usr/bin/env python
#encoding: utf-8

import os
import time
import HTMLTestRunner
import unittest
from selenium import webdriver
from appium import webdriver


from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



#class elementA(unittest.TestCase):
def runTest(self):
    pass

def setUp(self):
    desired_caps = {}
    desired_caps['deviceName'] = '114e53a3'  # adb devices查到的设备名
    #desired_caps['deviceName'] = 'iPhone 6'
    desired_caps['platformName'] = 'Android'
    #desired_caps['platformName'] = 'iOS'
    #desired_caps['platformVersion'] = '11.2.2'
    desired_caps['appPackage'] = 'com.modernsky.istv'  # 被测App的包名
    desired_caps['appActivity'] = 'com.modernsky.istv.ui.activity.LoadingActivity'  # 启动时的Activity

    #desired_caps['noReset'] = 'true'   # 不需要每次都安装apk
    desired_caps['automationName'] = 'Uiautomator2'

    #desired_caps['unicodeKeyboard'] = 'True'
    #desired_caps['resetKeyboard'] = 'True'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    time.sleep(8)


def tearDown(self):
    self.driver.quit()
    print('end ... ')