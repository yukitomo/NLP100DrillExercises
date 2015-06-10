#!/usr/bin/python
#-*-coding:utf-8-*-
#(96) 記事のタイトルとカテゴリ情報．複数のカテゴリが設定されているときは，全て抜き出せ

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
			print "title:",data
			self.flag_t = False
			
		if self.flag_c: #data = text のデータ
			pattern = re.compile(r'(\[\[)(Category:.+)(\]\])')
			match = pattern.search(data)
            if match:
                print match.group(2)
			
def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(open(sys.argv[1])) #../../../work/wiki/jawiki-latest-pages-meta-current.xml
	
if __name__=="__main__":
	main()