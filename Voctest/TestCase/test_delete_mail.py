# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: 111test_delete_mail.py
@ide: PyCharm Community Edition
@time: 2018-11-16 09:01
@blog: https://www.cnblogs.com/gotesting/

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC

class TestDelMail(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get('http://mail.goldencis.com/')

    def test_del_mail(self):

        # login
        self.dr.find_element_by_id('account_name').send_keys('jiaxy@goldencis.com')
        self.dr.find_element_by_id('password').send_keys('147258a?')
        self.dr.find_element_by_id('submit-btn').click()
        time.sleep(5)

        # 切换到 已发送
        self.dr.find_element_by_xpath('//*[@class="nui-tree-item-text"][@title="已发送"]').click()
        time.sleep(3)
        for i in range(0,1500):
            self.dr.find_element_by_xpath('//*[@class="js-component-icon nui-ico nui-ico-checkbox  "]').click()

            time.sleep(3)
            self.dr.find_element_by_xpath('//span[contains(text(),"删 除")]').click()
            time.sleep(3)
            i += 1

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()

