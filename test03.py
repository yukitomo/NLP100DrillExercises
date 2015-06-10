#!/usr/bin/python
#-*-coding:utf-8-*-
#(3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import sys

a = 0
f1=open('col1.txt','w')
f2=open('col2.txt','w')

for line in sys.stdin:
	itemList = line.strip().split('\t')
	if len(itemList) == 1 :
		itemList.append(" ") 
	f1.write(itemList[0]+"\n")
	f2.write(itemList[1]+"\n")

f1.close()
f2.close()


