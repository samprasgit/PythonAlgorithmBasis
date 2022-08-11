# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2022/08/11 09:51:44
@Desc    :   finally关键字的使用
"""

import smtplib


def send_email(host, port, user, password, sneder, receivers, message):
    """ 
    sned email specific email address
    """
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.login(user, password)
        server.sendmail(sneder, receivers, message.as_string())
        print("邮件发送成功")

    finally:
        # 使用finally处理异常
        # 清理服务器链接中的资源
        server.quit()


def write_file(file_name):
    """ 
    read given file by line
    """
    myfile = open(file_name)
    try:
        myfile.write("Python is awesome.")

    finally:
        myfile.close()
