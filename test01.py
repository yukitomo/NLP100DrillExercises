#!/usr/bin/python
#-*-coding:utf-8-*-
#(1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．
#標準入力から　cat address.txt | python test01.py
#確認 bash test01.sh

import sys
a = 0

for line in sys.stdin:
	a += 1

print a

