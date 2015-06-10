#!/usr/bin/python
#-*-coding:utf-8-*-

#(60) (57)の出力を「係り元」→「係り先」の有向グラフとみなし，Graphvizを使ってグラフを描画せよ．
#すなわち，(57)の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．
#グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい．

#cat test51_japanese.txt|python test57.py |python test60.py
#neato -Tsvg test60.dot

import sys
from collections import defaultdict

def main():
	f=open("test60.dot", "w")
	f.write('digraph "g" {\n')
	for line in sys.stdin:
		items = line.strip().split('\t')
		#print items
		if len(items) > 1:
			f.write('\t"'+items[0]+'" -> "'+items[1]+'" ;\n')
	f.write('}')

if __name__ == '__main__':
	main()