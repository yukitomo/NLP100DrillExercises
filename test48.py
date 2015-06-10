#!/user/bin/python
#-*-coding:utf-8-*-
#(48) 標準入力から読み込んだ各行の文字列の頻度を求めるプログラムを書き，
#(47)のプログラムと組み合わせることによって，文章中に出現する各動詞の出現頻度を求めよ．さらに，出現頻度の高い順に動詞を並べよ．
#python test47.py |python test48.py

import sys
from collections import defaultdict

count=defaultdict(lambda: 0)

for line in sys.stdin:
	count[line.strip()] += 1

for k, v in sorted(count.items(), key=lambda x:x[1], reverse=True):
	print k+" "+str(v)