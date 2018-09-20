#!/usr/bin/env python
#encoding: utf-8




import os
import time
import HTMLTestRunner
import unittest
import sys
import traceback


#from extend import Appium_Extend
from selenium import webdriver
sys.path.append(r'/Users/zhulx/Documents/jiaoben_z/initialization')   #将模块的路径添加到程序中
sys.path.append(r'/Users/zhulx/Documents/jiaoben_z/case_test')
sys.path.append(r'/jiaoben_z/Common/Test_Login')



import initialization
from Common.Test_Login import User_Login




from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TG_Ticket(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print('************************** start test **************************')

        # 初始化操作

    def setUp(self):
        initialization.setUp(self)


        # 测试用例执行完成后的操作


    def tearDown(self):
        initialization.tearDown(self)





    def is_toast_exist(self,text,result,timeout=30,poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            result = 1

        except:
            result = 0

        return result


        '''
            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            time.sleep(2)
            self.driver.tap([(338, 1197), (1014, 1364)])
            print(111111111)
            time.sleep(2)
            '''

        '''
            print('**********跳转支付页*********')
            self.driver.swipe(625,1666,682,216)
            '''

    #票务
    def buy_tickets(self):
        '''
        for i in range(4):
            self.driver.swipe(900,920,300,920)
        time.sleep(3)
        '''
        #用例执行成功时继续+截图
        #用例执行失败时截图+log+重新进入
        try:
            User_Login(self)

            time.sleep(5)

            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(1)
            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(2)



            #购票
            self.driver.find_element_by_id('com.modernsky.istv:id/mShop').click()

            # 多级目录截图
            foldname1 = time.strftime('%Y-%m-%d')

            dirname = os.path.join('/Users/zhulx/Documents/jiaoben_z/picture', foldname1)
            print(dirname)

            dirname2 = os.path.join(dirname, 'Test_Tickets')
            print(dirname2)

            if not os.path.exists(dirname):
                os.mkdir(dirname)

            if not os.path.exists(dirname2):
                os.mkdir(dirname2)


            else:
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

            time.sleep(1)

            #self.driver.swipe(700, 1520, 720, 451)
            #time.sleep(2)


            self.driver.find_element_by_id('com.modernsky.istv:id/ticket_name').click()
            print("********* 跳转演出详情页 **********")
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

            '''
            a = TG_Ticket
            a.is_toast_exist(self, "演出已结束卖票")
            '''

            '''
            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            time.sleep(2)
            self.driver.tap([(338,1197),(1014,1364)])
            '''
            print('hahahah')
            time.sleep(2)









            time.sleep(2)
            #self.driver.swipe(669, 1345, 669, 1000)
            #time.sleep(2)
            '''
            adb1 = 'adb shell input tap 921 1839'
            os.system(adb1)
            '''
            #self.driver.tap([767,1782][1071,1911], 2)
            self.driver.find_element_by_id('com.modernsky.istv:id/action').click()
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            print("********* 跳转选择票种页 **********")
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)



            self.driver.find_element_by_id("com.modernsky.istv:id/textView").click()  # 选择票种
            #self.driver.tap([(288,362),(645,483)])  # 选择时间 /  通过坐标(bound)定位点击
            time.sleep(2)
            self.driver.tap([(88,713),(294,768)])  # 选择时间 /  通过坐标(bound)定位点击
            #self.driver.find_element_by_id('com.modernsky.istv:id/scrollView').click()
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(1)
            '''
            self.driver.swipe(758,1606,758,1206)
            time.sleep(2)
            adb2 = 'adb shell input tap 531 1882'
            os.system(adb2)
            print('end')
            '''

            self.driver.find_element_by_id('com.modernsky.istv:id/txt_buy_ticket').click()
            time.sleep(2)

            a = TG_Ticket
            if a.is_toast_exist(self, "请选择票种",result=1):
                self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            else:
                self.driver.swipe(557,1565,690,308)
                time.sleep(2)

                '''
                self.driver.find_element_by_id('com.modernsky.istv:id/iv_ali_pay').click()
                print('**************** 选择支付宝 ****************')
                time.sleep(2)
                '''
                self.driver.find_element_by_id('com.modernsky.istv:id/tv_pay').click()
                print('**************** 跳转至微信支付 ****************')
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                #a.is_toast_exist(self, "请添加1位入场人")

                if a.is_toast_exist(self, "请添加1位入场人", result=1):
                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_addperson').click()
                    print('入场人未选择，进入入场人列表')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(2)
                    self.driver.find_element_by_id('com.modernsky.istv:id/mDefault').click()
                    print('选择入场人')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(1)
                    self.driver.find_element_by_id('com.modernsky.istv:id/mBtn').click()
                    print('入场人列表选择入场人点击确定跳转支付页')
                    time.sleep(2)
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_pay').click()
                    print('**************** 跳转至微信支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(3)
                    self.driver.press_keycode(4)  # 返回按键
                    self.driver.press_keycode(4)
                    time.sleep(2)
                    print('**************** 微信不支付返回商品订单列表，状态为待支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                    self.driver.find_element_by_id('com.modernsky.istv:id/ticket_name').click()
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    print('**************** 进入订单详情，交易状态为待支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    self.driver.swipe(525, 1580, 840, 328)
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    print('***************** 下滑页面，查看订单详情是否正确 ***************')
                    time.sleep(5)
                else:

                    self.driver.press_keycode(4)  # 返回按键
                    self.driver.press_keycode(4)
                    time.sleep(2)
                    print('**************** 微信不支付返回商品订单列表，状态为待支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                    self.driver.find_element_by_id('com.modernsky.istv:id/ticket_name').click()
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    print('**************** 进入订单详情，交易状态为待支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    self.driver.swipe(525, 1580, 840, 328)
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    print('***************** 下滑页面，查看订单详情是否正确 ***************')
                    time.sleep(5)



        except Exception as err:
            traceback.print_exc()
            print(err)
            print("*******异常********")




