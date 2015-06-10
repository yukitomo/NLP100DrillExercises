#!/usr/bin/python
#-*-coding:utf-8-*-
#(8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．
#sort -t $'\t' -k 2 address.txt

address = {}

for line in open("address.txt","r"):
	items = line.strip().split('\t')
	if len(items) == 1:
		items.append(" ")
	address[items[1]] = items[0]

for k,v in sorted(address.items(),key=lambda x:x[0]):
	print "%s\t%s" %(v, k)