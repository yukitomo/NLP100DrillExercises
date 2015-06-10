#!/usr/bin/python
#-*-coding:utf-8-*-
#(14)ツイッターのユーザー名（@で始まる文字列）を抽出せよ．

import sys
import re

pattern = re.compile(r'(@)([a-zA-Z0-9_]{1,}?)(?=:)')


for line in sys.stdin:
	match=pattern.search(line)
	if match:
		print match.group(2)