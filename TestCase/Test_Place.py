#!/usr/bin/env python
#encoding: utf-8




import os
import time
import HTMLTestRunner
import unittest
import sys
import traceback


from selenium import webdriver
sys.path.append(r'/Users/zhulx/Documents/jiaoben_z/initialization')   #将模块的路径添加到程序中
sys.path.append(r'/Users/zhulx/Documents/jiaoben_z/case_test')
sys.path.append(r'/jiaoben_z/Common/Test_Login')
sys.path.append(r'/jiaoben_z/Common/Screen_Shot')



import initialization
from Common.Test_Login import User_Login
from Common.Screen_Shot import shotPic




from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TG_Place(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print('************************** start test **************************')

        # 初始化操作

    def setUp(self):
        initialization.setUp(self)


        # 测试用例执行完成后的操作


    def tearDown(self):
        initialization.tearDown(self)




    def perform_places(self):

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

            dirname2 = os.path.join(dirname, 'Test_Place')
            print(dirname2)

            if not os.path.exists(dirname):
                os.mkdir(dirname)

            if not os.path.exists(dirname2):
                os.mkdir(dirname2)


            else:
                self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

            time.sleep(1)
            self.driver.tap([(161,82),(271,143)])
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/place_pic_near').click()
            print('************* 进入场地详情 **************')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)



            self.driver.find_element_by_id('com.modernsky.istv:id/place_goGps').click()
            print('************ 点击地图导航按钮 ************')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_cancel').click()
            print('************ 点击取消 ************')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/iconum').click()
            print('********** 点击场地演出旁的收藏按钮，收藏icon变蓝，收藏数+1 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/ticket_name').click()
            print('************ 点击场地演出，进入演出详情页，并查看收藏数按钮的状态与数量 *********** ')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            print('********** 点击返回，返回场地详情页 **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            #添加评论
            self.driver.find_element_by_id('com.modernsky.istv:id/action').click()
            print('********** 点击底部评论按钮，弹出输入框和键盘 ***********')
            time.sleep(1)
            self.driver.find_element_by_id('com.modernsky.istv:id/edittext').click()
            self.driver.find_element_by_id('com.modernsky.istv:id/edittext').send_keys('想去鸭')
            print('********* 想去鸭 ***********')
            time.sleep(3)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_edit_cancel').click()
            print('********* 发送评论，并最新评论下的第一条是否存在该评论 **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(5)
            self.driver.find_element_by_id('com.modernsky.istv:id/commentSave').click()
            print('********** 点赞 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)


            #回复自己的评论
            self.driver.find_element_by_id('com.modernsky.istv:id/mView').click()
            print('********** 点击自己的评论 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            self.driver.find_element_by_id('com.modernsky.istv:id/textView').click()
            print('********* 点击回复,弹出输入框和键盘 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/edittext').click()
            self.driver.find_element_by_id('com.modernsky.istv:id/edittext').send_keys('想去就去')
            print('********* 输入评论回复想去就去 ***********')
            time.sleep(3)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_edit_cancel').click()
            print('********* 发送回复，并最新评论下的第一条是否存在该回复 **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.tap([(66,1302),(1014,1355)])
            time.sleep(2)
            self.driver.tap([(171,1840),(909,1956)])
            print('********* 删除原评论,弹出二次确认的窗口 ********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_confirmation_no').click()
            print('********* 点击否，取消删除 ********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.tap([(66,1715),(1014,1768)])
            time.sleep(1)
            self.driver.tap([(171,1840),(909,1956)])
            print('********* 删除原评论,弹出二次确认的窗口 ********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_confirmation_yes').click()
            print('********* 点击是，删除原评论 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/place_pic_near').click()
            print('************* 重新进入场地详情，查看最新评论下回复引用的原评论是否删除 **************')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.swipe(563,1781,772,430)
            time.sleep(3)
            self.driver.find_element_by_id('com.modernsky.istv:id/contentLayout').click()
            print('********** 删除回复，弹出二次确认的窗口 **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            self.driver.tap([(171, 1840), (909, 1956)])
            print('********* 删除原评论,弹出二次确认的窗口 ********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/tv_confirmation_yes').click()
            print('********* 点击是，删除原评论 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(2)

            #self.driver.swipe(564,1737,793,275)
            #time.sleep(2)

            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.modernsky.istv:id/mPerson').click()
            print('********* 进入个人中心，查看消息显示未读数2 ***********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(1)
            self.driver.find_element_by_id('com.modernsky.istv:id/mMessage').click()
            print('********* 点击消息，进入消息列表，其中评论和点赞分别显示未读icon **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(1)
            self.driver.find_element_by_id('com.modernsky.istv:id/comment').click()
            print('********** 点击评论，进入评论列表 ***********')
            time.sleep(3)
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            self.driver.find_element_by_id('com.modernsky.istv:id/img_left_back').click()
            print('******** 返回评论列表 **********')
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')
            time.sleep(1)
            self.driver.find_element_by_id('com.modernsky.istv:id/saveMessage').click()
            print('******** 点击赞，进入点赞列表 ********')
            time.sleep(3)
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

























        except Exception as err:
            #traceback.print_exc()
            print(err)
            print("*******异常********")
            self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')

