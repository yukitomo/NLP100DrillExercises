#!/usr/bin/python
#-*-coding:utf-8-*-
#Stanford Core NLPのXML形式の出力から，以下の情報を抽出せよ．ただし，XML形式の解析にはlxmlモジュールを用いよ．
#91 ２番目の文の５番目のトークンの単語を抽出

from lxml import etree

xml_file = open('/Users/yukitomo/Study/anlp2014/yukitomo/set10_xml/corenlp_outpu.xml','r')
doc = etree.parse(xml_file )


for item in doc.xpath('//sentence[@id = "2"]/tokens/token[@id = "5"]/word'):
	print item.text

