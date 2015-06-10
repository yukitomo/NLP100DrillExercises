#!/usr/bin/python
#-*-coding:utf-8-*-
#(95) 記事にリダイレクト（転送）先が設定されているときは，記事のタイトルとリダイレクト先

import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.flag = False
		self.title_name = ""

	def startElement(self, name, attrs):
		if name == "redirect":
			print self.title_name.encode("utf-8") + "\t" +attrs.getValue("title").encode("utf-8")
		if name == "title":
			self.flag =True

	def endElement(self, name):
		if name == "title":
			self.flag = False
	
	def characters(self, data):
		if self.flag:
			self.title_name = data
			self.flag = False
			
def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(open(sys.argv[1])) #../../../work/wiki/jawiki-latest-pages-meta-current.xml
	
if __name__=="__main__":
	main()