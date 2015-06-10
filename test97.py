#!/usr/bin/python
#-*-coding:utf-8-*-
#(97) 記事のタイトルと対応する英語のページタイトル（言語間リンク）
#python test97.py /work/wikipedia/jawiki-latest-pages-meta-current.xml サーバで実行

import xml.sax
import xml.sax.handler
import sys
import re

class Handler(xml.sax.handler.ContentHandler):
        def __init__(self):
                self.flag_t = False
                self.flag_c = False
                self.title_name = ""
                self.category_name = ""

        def startElement(self, name, attrs):
                if name == "title":
                        self.flag_t =True

                if name == "text":
                        self.flag_c = True



        def endElement(self, name):
                if name == "title":
                        self.flag_t = False
                if name == "text":
                        self.flag_c = False

        def characters(self, data):
                if self.flag_t:
                        self.title_name = data
                        print data

                if self.flag_c: #data = text のデータ
                        pattern = re.compile(r'\{\{(Commonscat\|.+)\}\}')
                        match = pattern.search(data)
                        if match:
                                print match.group(1)

def main():
        parser = xml.sax.make_parser()
        parser.setContentHandler(Handler())
        parser.parse(open(sys.argv[1])) #../../../work/wiki/jawiki-latest-pages-meta-current.xml

if __name__=="__main__":
        main()