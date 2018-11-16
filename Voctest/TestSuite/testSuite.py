# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: testSuite.py
@ide: PyCharm Community Edition
@time: 2018-11-14 15:40
@blog: https://www.cnblogs.com/gotesting/

'''

import unittest
from TestCase import test_login
# from TestCase.test_login import TestLogin

suite = unittest.TestSuite()
loader = unittest.TestLoader()

# 通过加载测试类所在模块加载测试用例
suite.addTest(loader.loadTestsFromModule(test_login))


# 通过加载测试类来加载测试用例
# suite.addTest((loader.loadTestsFromTestCase(TestLogin)))