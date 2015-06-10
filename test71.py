#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, os, os.path, re 
from collections import defaultdict
from test62 import *
from geniatagger import *

#(71) ５つのファイル（英語のテキスト）にGENIA taggerを適用せよ．GENIA taggerは１文１行形式の入力を受け取るので，22のプログラムを再利用せよ．

#https://pypi.python.org/pypi/geniatagger-python/0.1

def output_genia_tagger(input_file, output_file, tagger,pattern):
	
	for line in open(input_file): #各テキストファイルの改行ごと
		if line.strip() != "": #空の行は無視

			#入力は一文にするために
			start = 0 #検索開始のインデックス
			while len(line) > start: #文字列の長さよりインデックスは小さくなければならない
				m = pattern.search(line,start)
				if m:
					sent = line[start:m.start()+1]
					start = m.end()-1
				else:
					sent = line[start:].strip()
					break
					
				for item in tagger.parse(sent): #[('This', 'This', 'DT', 'B-NP', 'O'), ('is', 'be', 'VBZ', 'B-VP', 'O'), ('a', 'a', 'DT', 'B-NP', 'O'), ('pen', 'pen', 'NN', 'I-NP', 'O'), ('.', '.', '.', 'O', 'O')]
					output_file.write("\t".join(item)+"\n") #形態素解析したものを書き込み
					#print "\t".join(item)
				output_file.write("EOS\n")
					#print "EOS"


def main():
	tagger = GeniaTagger('/Users/yukitomo/Software/geniatagger-3.0.1/geniatagger')
	pattern = re.compile(r'(\.\s[A-Z])|(\.\[[0-9]+\]\s[A-Z])')

	for input_file in file_paths_getter('sec8_english_texts', '.txt'):
		print "reding : %s"%input_file

		output_file = open(input_file+".genia","w") #書き込みファイル名
		output_genia_tagger(input_file, output_file, tagger, pattern)




if __name__ == "__main__":
	main()
	