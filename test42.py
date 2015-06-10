#!/user/bin/python
#-*-coding:utf-8-*-
#(42) 文章中に出現するすべての動詞を抜き出せ．

import pickle

def verb_extractor(text):
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["pos"]=="動詞":
				print text[m][n]["surface"]

def main():
	text = pickle.load(open("test41_output.pickle","r"))
	verb_extractor(text)

if __name__ == '__main__':
	main()
