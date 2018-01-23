# -*- coding:utf-8 -*-


class HtmlOutputer(object):
    def __init__(self):
        self.datas = list()

    def _sort_data(self):
        if len(self.datas) == 0:
            return
        self.datas.sort(key=lambda x: x['replies'], reverse=True)

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def collect_datas(self, datas):
        if datas is None or len(datas) == 0:
            return

        for data in datas:
            self.collect_data(data)

    def output_html(self):
        self._sort_data()

        fout = open('output.html', 'w')

        fout.write("<html><body><table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['replies'])
            fout.write("<td>%s</td>" % data['reads'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['url'])
            fout.write("</tr>")

        fout.write("</table></body></html>")

        fout.close()
