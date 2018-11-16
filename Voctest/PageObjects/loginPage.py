# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: loginPage.py
@ide: PyCharm Community Edition
@time: 2018-11-14 13:53
@blog: https://www.cnblogs.com/gotesting/

'''


class LoginPage:

    # 用户名输入框
    login_username = '//*[@class="gd-login-user"]'
    # 密码输入框
    login_passwd = '//*[@class="gd-login-password"]'
    # 登录按钮
    login_button = '//*[@class="gd-login-submit-bg"]'

    def __init__(self,driver,url):
        self.driver = driver
        self.driver.get(url)

    def login(self,username,passwd):
        self.driver.find_element_by_xpath(self.login_username).send_keys(username)
        self.driver.find_element_by_xpath(self.login_passwd).send_keys(passwd)
        self.driver.find_element_by_xpath(self.login_button).click()

