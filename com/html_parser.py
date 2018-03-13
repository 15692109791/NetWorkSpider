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
        # links1 = soup.find_all('a', href=re.compile(r"thread-[\w]*-[\w]*-[\w]*.html"))
        # for link in links1:
        #     new_url = link['href']
        #     new_full_url = urlparse.urljoin(url, new_url)
        #     new_urls.add(new_full_url)
        links2 = soup.find_all('a', href=re.compile(r"forum-[\d]+-[\d]+.html"))
        for link in links2:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_datas = list()
        tbody_rows = soup.find_all('tbody', id=re.compile(r"normalthread"))
        for topic_row in tbody_rows:
            title_node = topic_row.find('th', class_=re.compile(r"(common|new)"))
            num_node = topic_row.find('td', class_='num')
            res_data = dict()
            try:
                title = title_node.find('a').get_text()
                if title.find('料理') > -1:
                    reply = num_node.find('a').get_text()
                    read = num_node.find('em').get_text()
                    new_url = title_node.find('a')['href']
                    res_data['title'] = title
                    res_data['replies'] = int(reply)
                    res_data['reads'] = int(read)
                    new_full_url = urlparse.urljoin(url, new_url)
                    res_data['url'] = new_full_url
                    res_datas.append(res_data)
                    # if title.index('卡尔') >= -1 or title.index('祈求者') >= 0:
                    #     # if title.index('夜之魇') >= 0:
                    #     reply_node = topic_row.find('a', class_='replies')
                    #     res_data['replies'] = int(reply_node.get_text())
                    #
                    #     res_data['title'] = title
                    #     new_url = title_node['href']
                    #     new_full_url = urlparse.urljoin(url, new_url)
                    #     res_data['url'] = new_full_url
                    #     res_datas.append(res_data)
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
