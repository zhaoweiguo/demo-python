# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')

    pattern = re.compile('<div.*?author.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1],item[2],item[3],item[4]
    
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
