# -*- coding:utf-8 -*-
import sys
import re
import urlparse
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


class HtmlPaser(object):
    def _get_new_urls(self, url, soup):
        new_urls = set()
        links1 = soup.find_all('a', href=re.compile(r"/read.php\?tid="))
        for link in links1:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        links2 = soup.find_all('a', href=re.compile(r"/thread.php\?fid="))
        for link in links2:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_datas = list()
        topic_rows = soup.find_all('tr', class_='topicrow')
        for topic_row in topic_rows:
            title_node = topic_row.find('a', class_='topic')
            res_data = dict()
            title = title_node.get_text()
            try:
                if title.index('勇气') >= 0 and title.index('试炼') >= 0:
                    # if title.index('夜之魇') >= 0:
                    reply_node = topic_row.find('a', class_='replies')
                    res_data['replies'] = int(reply_node.get_text())

                    res_data['title'] = title
                    new_url = title_node['href']
                    new_full_url = urlparse.urljoin(url, new_url)
                    res_data['url'] = new_full_url
                    res_datas.append(res_data)
            except:
                pass
        return res_datas

    def parse(self, url, content_data):
        if url is None or content_data is None:
            return
        soup = BeautifulSoup(content_data, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data
