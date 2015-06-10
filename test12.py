#!/usr/bin/python
#-*-coding:utf-8-*-
#(12) 「なう」という文字列で終わるツイートを抽出せよ．
#python test12.py tweets.txt 

import sys
import re

pattern = re.compile(r'なう$')

for line in sys.stdin:
	if pattern.search(line):
		print line.strip()