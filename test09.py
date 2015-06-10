#!/usr/bin//python
#-*-coding:utf-8-*-
#(9) 各行を２コラム目，１コラム目の優先順位で辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）
#sort -d -r -k 2,1 address.txt

from collections import defaultdict

address = defaultdict(list)

for line in open("address.txt","r"):
	items = line.strip().split('\t')
	if len(items) == 1:
		items.append(" ")
	#2カラム目に対して、１カラム目をリストに格納
	address[items[1]].append(items[0])

#2カラム目でソート
for cal2,cal1s in sorted(address.items(),key=lambda x:x[0], reverse=True):
	for cal1 in sorted(cal1s, reverse=True):
		print cal1 +"\t" + cal2