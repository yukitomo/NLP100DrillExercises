#!/usr/bin/python
#-*-coding:utf-8-*-
#(15) ツイッターのユーザー名（例えば@xxxxxxx）を，そのユーザーのページへのリンク（<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>で囲まれたHTML断片）に置換せよ．
#cat ../data/tweets.txt |python test15.py 

import sys
import re

pattern1 = re.compile(r'(@)([a-zA-Z0-9_]{1,}?)(?=:)')

for line in sys.stdin:
	match1=pattern1.search(line)
	if match1:
		url='<a href="https://twitter.com/#!/xxxxxxx">@xxxxxxx</a>'
		dst = url.replace('xxxxxxx',match1.group(2))
		print line.replace(match1.group(2),dst)