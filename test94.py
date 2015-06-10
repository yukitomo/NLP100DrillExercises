#!/usr/bin/python
#-*-coding:utf-8-*-
#(94) 記事のタイトル

import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.flag = False
	def startElement(self, name, attrs):
		if name == "title":
			self.flag =True

	def endElement(self, name):
		if name == "title":
			self.flag = False
	
	def characters(self, data):
		if self.flag:
			self.title_name = data
			print data.encode("utf-8")

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.parse(open(sys.argv[1]))
	
if __name__=="__main__":
	main()