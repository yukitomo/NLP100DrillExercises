#!/usr/bin/python
#-*-coding:utf-8-*-
#(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ
#はじめに f = ~ で読み込まないほうがメモリ的によい

import sys
n= int(sys.argv[1])
i = 0

for line in sys.stdin:
	if i == n+1:
		break
	print line,
	i += 1
	



