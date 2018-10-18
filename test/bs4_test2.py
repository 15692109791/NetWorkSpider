# -*- coding:utf-8 -*-
import urllib2

from bs4 import BeautifulSoup

f = open('d:/myspace/network-spider/test/view-source_https___www.baidu.com.html', 'r')
html_doc = f.read()
f.close()

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

# 获取class=s_tab的div下，a标签的数量
print '获取class=s_tab的div下，a标签的数量'
div_node = soup.find('div', class_='s_tab')
all_link = div_node.find_all('a')
print len(all_link)
