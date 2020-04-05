#!/usr/bin/python

import sys
import pycurl


def body(buf):
    sys.stdout.write(buf)


def header(buf):
    sys.stdout.write(buf)


c = pycurl.Curl()
c.setopt(pycurl.URL, "www.baidu.com")   # 设置要访问的网址
c.setopt(pycurl.WRITEFUNCTION, body)    # 调用body()函数来输出返回的信息
c.setopt(pycurl.HEADERFUNCTION, header) # 调用header()函数来输出返回的信息
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.perform()   # 执行
c.close()

