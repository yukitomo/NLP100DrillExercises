#!/usr/bin/python
#-*-coding:utf-8-*-
#(93) １番目の文の４番目のトークンの，係り受け構造上での子（dependent）の単語

from lxml import etree

xml_file = open('/Users/yukitomo/Study/anlp2014/yukitomo/set10_xml/corenlp_outpu.xml','r')
doc = etree.parse(xml_file)

pr = 0
for dep in doc.xpath('//sentence[@id = "1"]/dependencies[@type = "basic-dependencies"]/dep'):
	#print etree.tostring(dep)
	for item in dep:
		if pr == 1:
			print item.text
			pr = 0
		if item.tag == 'governor' and item.get('idx')=='4':
			pr =1

