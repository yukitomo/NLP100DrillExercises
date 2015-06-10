#!/usr/bin/python
#-*-coding:utf-8-*-
#(6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ

import sys
n= int(sys.argv[1])
f=open("address.txt","r")
itemList=[]


for line in f:
	itemList.append(line)

for k in range(n):
	print itemList[len(itemList)-n+k],
