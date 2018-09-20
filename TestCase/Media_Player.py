#!/usr/bin/env python
#encoding: utf-8



import time
import sys
import unittest
import traceback



sys.path.append('/jiaoben_z/initialization')
sys.path.append('/jiaoben_z/Common/Test_Login')

import initialization
from Common.Test_Login import User_Login






class TG_Media(unittest.TestCase):
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print('************************** start test **************************')

        # 初始化操作

    def setUp(self):
        initialization.setUp(self)

        # 测试用例执行完成后的操作

    def tearDown(self):
        initialization.tearDown(self)



    def video_play(self):

        try:
            User_Login(self)
            time.sleep(3)

            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(1)
            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(2)

            #self.driver.swipe(583,1620,542,574)
            #time.sleep(2)
            self.driver.find_element_by_id("com.modernsky.istv:id/img_video_channel_pic").click()
            print("进入点播播放页")
            time.sleep(5)


        except Exception as err:
            traceback.print_exc()
            print(err)
            print("*******异常********")
