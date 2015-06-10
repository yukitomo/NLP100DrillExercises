#!/usr/bin/python
#-*-coding:utf-8-*-
#(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．
#cut -f 2 address.txt|sort | uniq -c | sort -k 1 -r > test10_2.result

from collections import defaultdict



def word_counter(input_file):
	col2 = defaultdict(int)
	for line in input_file:
		col2[line.strip()] += 1  
	return col2

def top_n_order(word_counts,n):
	if n == 0:
		for k,v in sorted(word_counts.items(),key=lambda x:x[1], reverse = True):
			print k ,v
	else:
		i = 0
		for k,v in sorted(word_counts.items(),key=lambda x:x[1], reverse = True):
			print k ,v
			i += 1
			if i == n-1:
				break

def main():
	f = open("col2.txt","r")
	word_counts = word_counter(f)
	top_n_order(word_counts,100)




if __name__ == '__main__':
	main()