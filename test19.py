#!/usr/bin/python
#-*-coding:utf-8-*-
#(19) 郵便番号・県名・市町村名の３要素を組で（まとめて）抽出せよ．
#python test19.py tweet.txt
import sys 
import re

pattern = re.compile(u'(\d{3}\-\d{4})*(北海道|東京都|(大阪|京都)府|(神奈川|和歌山|鹿児島)県|[^\s\w\d　]{2}県)([^\s\w\d　]{1,6}[市郡区町村])')

for line in sys.stdin:
	line = line.decode("utf-8")
	match=pattern.search(line)
	if match:
		print match.group(0).encode("utf-8")
		