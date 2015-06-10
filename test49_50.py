#!/usr/bin/python
#-*-coding:utf-8-*-
#(49) (48)の出力を利用して，文字列の頻度を横軸，その文字列の異なり数（種類数）を縦軸として，ヒストグラムをプロットせよ．
#なお，プロットにはgnuplotやmatplotlibを用い，グラフを画像ファイルとして保存せよ
#(50) (48)の出力を利用して，文字列の出現頻度の順位（高い順）を横軸，その出現頻度を縦軸として，プロットせよ

import sys
import matplotlib.pyplot as plt
from collections import defaultdict

data=[]
word_count=defaultdict(lambda: 0)
for line in sys.stdin:
	items=line.strip().split()
	word_count[items[0]]=int(items[1])
	data.append(int(items[1]))

#49 x:文字列の頻度, y:文字列の異なり数
plt.hist(data,bins=100,range=(0,50))
plt.savefig("test49_output.png")

#50 x:文字列の頻度の高い順位, y:出現頻度
p=[]
q=[]
order=1
for k,v in sorted(word_count.items(), key=lambda x:x[1], reverse=True):
	p.append(order)
	q.append(v)
	order += 1
fig2, axes2 = plt.subplots(figsize=(7,4)) 
axes2.plot(p, q, 'r')
plt.xlim(0,100)
plt.savefig("test50_output.png")
plt.show()

