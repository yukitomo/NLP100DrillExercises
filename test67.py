#!/usr/bin/python
#-*-coding:utf-8-*-
#(67) 66の出力の各行を名詞句の（疎）ベクトルとみなし，「日本」と「我が国」のベクトル間の内積（コサイン類似度）を求めよ．

#python test67.py

import sys,pickle
from collections import defaultdict


def cos_similarity(vectors_dict,word1,word2):
	vec1 = vectors_dict[word1]
	vec2 = vectors_dict[word2]

	similarity = 0

	for element_idx in vec1.keys():
		similarity += vec1.get(element_idx,0) * vec2.get(element_idx,0)

	return similarity

def main():
	vectors_dict = pickle.load(open("test66_np_vectors.pkl","r")) #test66の各ベクトルを格納したもの

	word1 = raw_input("word1 = ")
	word2 = raw_input("word2 = ")
	similarity = cos_similarity(vectors_dict,word1,word2)
	print "cos_similarity = %f"%similarity

if __name__ == "__main__":
	main()