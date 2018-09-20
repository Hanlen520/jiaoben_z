#!/usr/bin/env python
#encoding: utf-8



import os
import time
import HTMLTestReportCN
import unittest
import sys



#from extend import Appium_Extend
from selenium import webdriver
sys.path.append(r'/jiaoben_z/initialization')   #将模块的路径添加到程序中
sys.path.append(r'/jiaoben_z/TestCase/Test_Ticket')
sys.path.append(r'/jiaoben_z/TestCase/Test_Goods')
sys.path.append(r'/jiaoben_z/TestCase/Test_Place')
sys.path.append(r'/jiaoben_z/Testcase/Test_banner')



import initialization
from TestCase import Test_Ticket
from TestCase import Media_Player
from TestCase import Test_Goods
from TestCase import Test_Place
from TestCase import  Test_banner



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))




'''
class elementB(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print('************************** start test **************************')

    # 初始化操作
    def setUp(self):
        initialization.setUp(self)

    # 测试用例执行完成后的操作
    def tearDown(self):
        initialization.tearDown(self)


    def test(self):
        Test_Ticket.buy_tickets(self)
    def test_1(self):
        Media_Player.video_play(self)
'''



if __name__ == '__main__':

    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    for i in range(1):

        #testunit.addTest(elementB('swipeLeft'))
        #testunit.addTest(('test'))  # 将测试用例加入到测试容器中
        #testunit.addTest(Media_Player.TG_Media('video_play'))
        testunit.addTest(Test_Ticket.TG_Ticket('buy_tickets'))
        #testunit.addTest(Test_Place.TG_Place('perform_places'))
        #testunit.addTest(Test_Goods.TG_Goods('buy_goods'))
        #testunit.addTest(Test_banner.TG_Banner('banner_jump'))
    timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = '/Users/zhulx/Documents/jiaoben_z/TestReport/' + timestr + '.html'  # 这个路径改成自己的目录路径
    #filename = '/Users/zhulx/Documents/test_result/myAppiumLog.html'  # 定义个报告存放路径，支持相对路径。
    fp = open(filename,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='Test Report',description='每个用例执行的结果与详情')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)  # 自动进行测试
    fp.close()




