#!/usr/bin/env python
# encoding: utf-8


import os
import time
import HTMLTestRunner
import unittest
import sys
import traceback

# from extend import Appium_Extend
from selenium import webdriver

sys.path.append(r'/jiaoben_z/initialization')  # 将模块的路径添加到程序中
sys.path.append(r'/jiaoben_z/case_test')

sys.path.append(r'/jiaoben_z/Common/Test_Login')



import initialization
from Common.Test_Login import User_Login


from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TG_Goods(unittest.TestCase):


        def __init__(self, methodName):
            unittest.TestCase.__init__(self, methodName)
            print('************************** start test **************************')

            # 初始化操作

        def setUp(self):
            initialization.setUp(self)

            # 测试用例执行完成后的操作

        def tearDown(self):
            initialization.tearDown(self)



        def is_toast_exist(self, text, result, timeout=30, poll_frequency=0.5):
            try:
                toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
                WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
                result = 1

            except:
                result = 0

            return result




        def buy_goods(self):
            try:


                User_Login(self)

                time.sleep(5)



                self.driver.find_element_by_id('android:id/button1').click()
                time.sleep(1)
                self.driver.find_element_by_id('android:id/button1').click()
                time.sleep(2)

                self.driver.find_element_by_id('com.modernsky.istv:id/mShop').click()



                # 多级目录截图
                foldname1 = time.strftime('%Y-%m-%d')

                dirname = os.path.join('/Users/zhulx/Documents/jiaoben_z/picture', foldname1)
                print(dirname)

                dirname2 = os.path.join(dirname, 'Test_Goods')
                print(dirname2)

                if not os.path.exists(dirname):
                    os.mkdir(dirname)

                if not os.path.exists(dirname2):
                    os.mkdir(dirname2)

                else:
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')



                time.sleep(3)
                self.driver.tap([(306, 98), (426, 159)])
                time.sleep(3)
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                self.driver.find_element_by_id('com.modernsky.istv:id/iv_head').click()
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                time.sleep(2)
                print('**************** 进入新款草莓周边列表 ****************')
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                self.driver.find_element_by_id('com.modernsky.istv:id/iv_goods').click()
                print('**************** 进入商品详情 ****************')
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                time.sleep(5)

                # 加入购物车
                self.driver.find_element_by_id('com.modernsky.istv:id/tv_put_cart').click()
                print('**************** 点击加入购物车，弹出商品规格选择窗口，默认选择 ****************')
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                self.driver.find_element_by_id('com.modernsky.istv:id/tv_buy_other').click()

                a = TG_Goods
                if a.is_toast_exist(self, "请选择规格", result=1):
                    self.driver.find_element_by_id('com.modernsky.istv:id/iv_close').click()
                    time.sleep(1)
                    self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
                    print('************ 该商品所有型号规格已置灰，返回商品列表 ***********')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(2)
                    self.driver.tap([(17, 964), (523, 1410)])
                    print('************* 点击第三个未售罄的商品 **********')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(3)

                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_put_cart').click()
                    print('**************** 点击加入购物车，弹出商品规格选择窗口，默认选择 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                    time.sleep(2)

                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_buy_other').click()
                    print('**************** 点击确定，商品详情页弹出toast加入购物车成功 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(3)

                    self.driver.find_element_by_id('com.modernsky.istv:id/iv_cart').click()
                    print('**************** 进入购物车进行对比是否添加成功 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                    time.sleep(3)

                    self.driver.find_element_by_id('com.modernsky.istv:id/cb_check_cart').click()
                    print('购物车勾选商品')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(2)

                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_pay_cart').click()
                    print('**************** 从购物车选择商品跳转去支付页 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                    time.sleep(3)

                    self.driver.find_element_by_id('com.modernsky.istv:id/tv_pay').click()
                    print('**************** 跳转至微信支付 ****************')
                    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

                    if a.is_toast_exist(self, "亲，您还有几个待支付的商品订单，先去清空一下吧", result=1):

                        for i in range(4):
                            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
                            time.sleep(1)

                        self.driver.find_element_by_id('com.modernsky.istv:id/mPerson').click()
                        time.sleep(1)
                        self.driver.find_element_by_id('com.modernsky.istv:id/mOrder').click()
                        time.sleep(2)
                        self.driver.find_element_by_id('com.modernsky.istv:id/titleTxt').click()
                        print('************* 进入我的商品订单 *************')
                        self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
                        time.sleep(2)
                        self.driver.find_element_by_id('com.modernsky.istv:id/tv_next').click()
                        print('************* 点击去支付，进入该商品的订单详情 *************')
                        time.sleep(2)
                        self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')





                else：










            except Exception as err:
                # traceback.print_exc()
                print(err)
                print("*******异常********")
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')



