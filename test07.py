#!/usr/bin/python
#-*-coding:utf-8-*-
#(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．
#line.split("t", 必要なカラム数)で

itemList=[]

for line in open("col1.txt","r"):
	itemList.append(line.strip())

print len(set(itemList))
