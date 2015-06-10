#!/usr/bin/python
#-*-coding:utf-8-*-
#(11) 「拡散希望」という文字列を含むツイートを抽出せよ．
#cat tweets.txt | grep 拡散希望| wc -l
#python test11.py tweets.txt | wc -l
#endswithのほうがはやい

import sys
import re

pattern = re.compile(r'拡散希望')

for line in sys.stdin:
	if pattern.search(line):
		print line.strip()

