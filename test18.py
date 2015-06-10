#!/usr/bin/python
#-*-coding:utf-8-*-
#(18) 仙台市の住所らしき表現にマッチする正規表現を各自で設計し，抽出せよ．
#python test18.py tweet.txt 

import sys 
import re

pattern = re.compile(u'(仙台市)([^\s\w\d　]{1,20}[\d０-９〇一-九十上下東西]+)*')

for line in sys.stdin:
	line = line.decode("utf-8")
	match=pattern.search(line)
	if match:
		print match.group(0).encode("utf-8")