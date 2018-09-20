#!/usr/bin/env python
#encoding: utf-8



import time
import sys
import unittest
import traceback
import os



sys.path.append('/jiaoben_z/initialization')
sys.path.append('/jiaoben_z/Common/Test_Login')

import initialization
from Common.Test_Login import User_Login






class TG_Banner(unittest.TestCase):
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print('************************** start test **************************')

        # 初始化操作

    def setUp(self):
        initialization.setUp(self)

        # 测试用例执行完成后的操作

    def tearDown(self):
        initialization.tearDown(self)



    def banner_jump(self):

        try:
            User_Login(self)
            time.sleep(3)

            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(1)
            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(2)

            # 多级目录截图
            foldname1 = time.strftime('%Y-%m-%d')

            dirname = os.path.join('/Users/zhulx/Documents/jiaoben_z/picture', foldname1)
            print(dirname)

            dirname2 = os.path.join(dirname, 'Test_banner')
            print(dirname2)

            if not os.path.exists(dirname):
                os.mkdir(dirname)

            if not os.path.exists(dirname2):
                os.mkdir(dirname2)


            else:
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')



            # 媒资首页banner跳转


            for i in range(5):
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                self.driver.find_element_by_id('com.modernsky.istv:id/banner').click()
                time.sleep(3)
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                print('************ 跳转媒资首页banner详情 **************')
                self.driver.press_keycode(4)
                time.sleep(3)
                self.driver.swipe(824,424,156,612)
            time.sleep(3)

            # 票务首页banner跳转
            self.driver.find_element_by_id('com.modernsky.istv:id/mShop').click()
            print('*********** 跳转票务首页 *************')
            time.sleep(2)
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            for i in range(8):
                self.driver.find_element_by_id('com.modernsky.istv:id/banner').click()
                time.sleep(2)
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                print('************ 跳转票务首页banner详情 **************')
                self.driver.press_keycode(4)
                time.sleep(3)
                self.driver.swipe(824, 424, 156, 612)
            time.sleep(3)

            #商城首页banner跳转
            self.driver.tap([(306, 98), (426, 159)])
            print('*********** 跳转商城首页 *************')
            time.sleep(2)
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            for i in range(8):
                self.driver.find_element_by_id('com.modernsky.istv:id/banner').click()
                time.sleep(2)
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                print('************ 跳转商城首页banner详情 **************')
                self.driver.press_keycode(4)
                time.sleep(3)
                self.driver.swipe(824, 424, 156, 612)
            time.sleep(3)









        except Exception as err:
            traceback.print_exc()
            print(err)
            print("*******异常********")
