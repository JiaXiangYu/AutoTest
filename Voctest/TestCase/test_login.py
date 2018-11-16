# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: test_login.py
@ide: PyCharm Community Edition
@time: 2018-10-31 16:44
@blog: https://www.cnblogs.com/gotesting/

'''

import unittest
import time
import traceback
from PageObjects.loginPage import LoginPage
from selenium import webdriver
from Common.log import Log

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.logger = Log()
        self.logger.log_info('「Login Test Start：')
        url = 'http://10.10.15.153'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver,url)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        self.logger.log_info('_Login Test End」')

    # 登录成功
    def test_1_login_success(self):
        self.lp.login('system','123456')
        time.sleep(3)
        try:
            msg = self.driver.find_element_by_xpath('//*[@class="gd-topbar-tool-text"]').text
            self.assertEquals('system',msg)
            self.logger.log_info('Test Case "test_1_login_success" Passed !')
        except Exception as e:
            self.logger.log_error('Test Case "test_4_login_fail" Failed ! \n{0}'.format(e))
            raise e

    # 无用户名登录
    def test_2_login_no_username(self):
        self.lp.login('','123456')
        time.sleep(3)
        try:
            msg = self.driver.find_element_by_xpath('//*[@class="gd-login-submit-text"]').text
            self.assertEquals('登 录',msg)
            self.logger.log_info('Test Case "test_2_login_no_username" Passed !')
        except Exception as e:
            self.logger.log_error('Test Case "test_4_login_fail" Failed ! \n{0}'.format(e))
            raise e


    # 无密码登录
    def test_3_login_no_passwd(self):
        self.lp.login('system','')
        time.sleep(3)
        msg = self.driver.find_element_by_xpath('//*[@class="gd-login-submit-text"]').text
        try:
            msg = self.driver.find_element_by_xpath('//*[@class="gd-login-submit-text"]').text
            self.assertEquals('登 录',msg)
            self.logger.log_info('Test Case "test_3_login_no_passwd" Passed !')
        except Exception as e:
            self.logger.log_error('Test Case "test_4_login_fail" Failed ! \n{0}'.format(e))
            raise e


    # 用户名/密码错误
    def test_4_login_fail(self):
        self.lp.login('system','1234567890')
        time.sleep(3)
        try:
            msg = self.driver.find_element_by_xpath('//*[@class="gd-login-msg"]').text
            self.assertEquals('用户名或密码错误',msg)
            self.logger.log_info('Test Case "test_4_login_fail" Passed !')
        except Exception as e:
            self.logger.log_error('Test Case "test_4_login_fail" Failed ! \n{0}'.format(e))
            raise e

