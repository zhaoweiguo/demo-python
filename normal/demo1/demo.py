#!/usr/local/bin/python
"""
# 把nginx日志文件中,13年08月的所有文件中有字串"basewifi.747"的条数打印出来
# 格式: <日期>:  <有basewifi.747的个数>
"""

import string

i = 15
count = 0
substring = "basewifi.747"
while i < 27:
    print(i)
    i = i+1
    path = "/var/log/nginx/2013/08/access.201308" + str(i) + ".log"
    print(path)
    f = open(path, 'r')   # 打开读日志文件(以读模式)
    w = open("/usr/home/wolf/tmp/basewifi.log", 'a')    # 打开日志文件(以append方式打开)
    w.write(str(i)+":   ")     # 往日志文件写入日期
    line = True
    while line:    # 对指定文件进行遍历,计算出有"basewifi.747"的个数
        line = f.readline()      # 读一行文件内容
        if string.find(line, substring) != -1:    # 文件中是否有"basewifi.747"字串
            count = count + 1

    w.write(str(count) + " \n")

f.close()
w.close()