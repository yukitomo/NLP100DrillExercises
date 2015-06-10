#!/usr/bin/python
#-*-coding:utf-8-*-
#(25) (24)の出力を標準入力から１行（１単語）を読み込む毎に，その単語を小文字に変換した文字列を各行の最終列にタブ区切り形式で追加し，標準出力に書き出せ．

import sys
import re

for token in sys.stdin:
	print token.strip()+"\t"+token.lower(),