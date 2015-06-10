#!/usr/bin/python
#-*-coding:utf-8-*-
#(17) 人名らしき表現にマッチする正規表現を各自で設計し，抽出せよ．（例えば「さん」「氏」「ちゃん」などの接尾辞に着目するとよい）


import sys
import re

pattern = re.compile(u'([一-龠]{2,5})(さん|氏|ちゃん)')


for line in sys.stdin:
	line = line.decode("utf-8")
	match=pattern.search(line)
	if match:
		print match.group(0).encode("utf-8")