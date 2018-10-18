# -*- coding:utf-8 -*-
import re

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

# 打印所有信息
print '打印所有节点'
all_link = soup.find_all('a')
for link in all_link:
    print link.name, link['href'], link.get_text()

# 正则表达式匹配
print '正则表达式'
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

# 获取P段落
print '获取P段落文字'
p_node = soup.find('p', class_='story')
print p_node.name, p_node.get_text()

# 打印a标签的数量
print '打印a标签的数量'
all_link = soup.find_all('a')
print len(all_link)

