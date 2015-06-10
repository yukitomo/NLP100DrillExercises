#!/usr/bin/python
#-*-coding:utf-8-*-
#(36) １行１単語形式（medline.txt.sent.tok）を読み込み，単語の連接を出力するプログラムを実装せよ．ただし，出力形式は"(現在の単語)\t(次の単語)"とせよ．
#cat medline.txt.sent.tok | python test36.py

import sys

def main():
	pre_word = ""
	next_word = ""
	for line in sys.stdin:
		next_word=line.strip()
		if pre_word != "" :
			print "%s\t%s"%(pre_word,next_word)
			if next_word == "." or next_word == "!" or next_word == ",":
				pre_word = ""
			else:
				pre_word = next_word
		else:
			pre_word = next_word

if __name__ == '__main__':
	main()