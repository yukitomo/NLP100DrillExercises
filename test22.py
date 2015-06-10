#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re 

pattern = re.compile(r'\.\s[A-Z]')
#text = open(sys.argv[1])

for line in sys.stdin:
	start = 0 #検索開始のインデックス
	while len(line) > start: #文字列の長さよりインデックスは小さくなければならない
		m = pattern.search(line,start)
		if m:
			print line[start:m.start()+1]
			start = m.end()-1
		else:
			print line[start:].strip()
			break
		
