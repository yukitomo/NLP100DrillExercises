#!/usr/bin/python
#-*-coding:utf-8-*-
#(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#cat address.txt | python test02.py
#確認 bash test2.sh

import sys

for line in sys.stdin:
	print line.replace("\t"," ").strip()

