#!/usr/bin/python
#-*-coding:utf-8-*-
#(43) 文章中に出現するすべての動詞の基本形を抜き出せ．

import pickle

def verb_base_extractor(text):
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["pos"]=="動詞":
				print text[m][n]["base"]+"\n",	

def main():
	text = pickle.load(open("test41_output.pickle","r"))
	verb_base_extractor(text)

if __name__ == '__main__':
	main()

