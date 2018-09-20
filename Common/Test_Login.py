#!/usr/bin/env python
#encoding: utf-8


import time
import os
import datetime


def User_Login(self):
    # 登录
    # 输入用户名
    # a = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView").text
    # if "登 录" in a:
    print("**************** 进入登录页面 ****************")
    time.sleep(1)
    self.driver.find_element_by_id('com.modernsky.istv:id/mChange').click()
    print("**************** 进入密码页面 ****************")


    #多级目录截图
    foldname1 = time.strftime('%Y-%m-%d')

    dirname = os.path.join('/Users/zhulx/Documents/jiaoben_z/picture',foldname1)
    print(dirname)

    dirname2 = os.path.join(dirname, 'Test_Login')
    print(dirname2)

    if not os.path.exists(dirname):
        os.mkdir(dirname)



    if not os.path.exists(dirname2):
        os.mkdir(dirname2)


    else:
        self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') + '.png')



    time.sleep(2)

    # 输入手机号
    self.driver.find_element_by_id('com.modernsky.istv:id/mEditPhone').send_keys('17611235179')

    # 输入密码
    self.driver.find_element_by_id('com.modernsky.istv:id/mEditPwd').click()
    self.driver.find_element_by_id('com.modernsky.istv:id/mEditPwd').send_keys('111111')
    time.sleep(1)

    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') +'.png')

    # 点击登录按钮
    # self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @index='3']").click()

    self.driver.find_element_by_id('com.modernsky.istv:id/mLogin').click()
    # self.driver.find_element_by_xpath("//*[@class='android.widget.TextView'][3]").click()

    time.sleep(2)
    self.driver.get_screenshot_as_file(dirname2 + '/' + time.strftime('%H:%M:%S') +'.png')
    print("**************** 登录成功 ****************")
