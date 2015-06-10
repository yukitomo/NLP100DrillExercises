#!/usr/bin/python
#-*-coding:utf-8-*-
#(20) ツイートから絵文字らしき文字列を抽出せよ
#python test20.py tweet.txt

import sys 
import re

pattern = re.compile(r'\([^一-額ぁ-んァ-ヴ]{3,6}\)')


for line in sys.stdin:
	match = pattern.search(line)
	if pattern.search(line) :
		print match.group(0)
