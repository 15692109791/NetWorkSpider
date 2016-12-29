# -*- coding:utf-8 -*-
import url_manager, html_parser, html_downloader, html_outputer
from frame.config import ROOT_URL, MAX_COUNT


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlPaser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # -- 将根目录加入url管理器 --
        self.urls.add_new_url(root_url)
        # -- 循环处理管理器中的url --
        count = 1
        while self.urls.has_new_url():
            try:
                # -- 获取一个新的url --
                new_url = self.urls.get_new_url()
                print "craw %d : %s  %d" % (count, new_url, len(self.outputer.datas))
                # -- 下载页面信息 --
                download_content = self.downloader.download(new_url)
                # -- 解析信息，获取相关链接和有效数据 --
                urls, content_datas = self.parser.parse(new_url, download_content)
                # -- 将新的链接加入url管理器，数据加入收集器 --
                self.urls.add_new_urls(urls)
                self.outputer.collect_datas(content_datas)

                if count >= MAX_COUNT:
                    break
                count += 1
            except:
                print "craw failed"
        self.outputer.output_html()


if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw(ROOT_URL)
