# -*- coding:utf-8 -*-

'''
@project: Voctest
@author: Jimmy
@file: sendMail.py
@ide: PyCharm Community Edition
@time: 2018-11-15 17:14
@blog: https://www.cnblogs.com/gotesting/

'''

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Common.log import Log
from Config.globalConfig import report_path


logger = Log()
# 配置收发件人
recv_address = ['641969198@qq.com']
# 163的用户名和密码
send_addr_name = 'jxy641969198@163.com'
send_addr_pswd = 'jiaxy19920319'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recv_address
        else:
            self.sendTo = recver

    def get_report(self):
        """获取最新测试报告"""
        lists = os.listdir(report_path)
        lists.sort()
        send_report = lists[-1]
        print('The send report name: {0}'.format(send_report))
        return send_report

    def take_messages(self):
        """生成邮件的内容，和html报告附件"""
        report = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'VOC自动化测试报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(report_path, report), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="VocAutoTestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.take_messages()
        self.msg['from'] = send_addr_name
        try:
            smtp = smtplib.SMTP('smtp.163.com', 25)
            smtp.login(send_addr_name, send_addr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.log_info("发送邮件成功")
        except Exception:
            logger.log_error('发送邮件失败')
            raise