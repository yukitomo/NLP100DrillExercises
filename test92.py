#!/usr/bin/python
#-*-coding:utf-8-*-
#Stanford Core NLPのXML形式の出力から，以下の情報を抽出せよ．ただし，XML形式の解析にはlxmlモジュールを用いよ．
#(92) １番目の文のlemmaを並べたもの

from lxml import etree

xml_file = open('/Users/yukitomo/Study/anlp2014/yukitomo/set10_xml/corenlp_outpu.xml','r')
doc = etree.parse(xml_file)


for item in doc.xpath('//sentence[@id = "1"]/tokens/token/lemma'):
	print item.text+" ", 

