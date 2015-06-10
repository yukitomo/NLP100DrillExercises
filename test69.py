#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
from test53 import *

#cat test68_output.txt |python test69.py 
#neato -Tsvg test69.dot
#(69) 68の結果を名詞句をノードとする無向グラフとみなし，Graphvizを使ってグラフを描画せよ．すなわち，68の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい．

def main():
	write_file = open("test69.dot", "w")

	write_file.write('graph "g" {\n')
	for line in sys.stdin:
		items = line.strip().split('\t') #test68_output.txt

		if len(items) > 1:
			write_file.write('\t"'+items[1]+'" -- "'+items[2]+'" ;\n')

	write_file.write('}')

if __name__ == '__main__':
	main()
