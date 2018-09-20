#!/usr/bin/env python
#encoding: utf-8


import time
from selenium import webdriver




def shotPic(self):
    picname = '/jiaoben_z/picture/' + time.strftime('%H:%M:%S')
    self.driver.get_screenshot_as_file( + picname + '.png')
