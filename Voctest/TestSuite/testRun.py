# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: testRun.py
@ide: PyCharm Community Edition
@time: 2018-11-14 15:49
@blog: https://www.cnblogs.com/gotesting/

'''

import unittest
import HTMLTestRunner
import time

from Config.globalConfig import *
from TestSuite import  testSuite
from Common.log import Log
from Common.sendMail import SendMail

def run_test():


    runner = unittest.TextTestRunner()
    curTime = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_name = report_path + '\\' + 'TestResult-' + curTime + '.html'
    with open(report_name,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = f,
            title = '测试报告'
        )
        runner.run(testSuite.suite)

    time.sleep(3)
    mail = SendMail()
    mail.send()

if __name__ == '__main__':
    logger = Log()
    logger.log_info('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- Auto  Test  Comming -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    run_test()
    logger.log_info('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- Auto  Test  Done -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')