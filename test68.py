#!/usr/bin/python
#-*-coding:utf-8-*-
#(68) すべての名詞句のペアに対し，文脈ベクトルの内積が0.6以上のペアをすべて抜きだし，内積値が大きい順に並べよ．
#このとき，出力形式は"(内積値)\t(名詞句1)\t(名詞句2)\n"とせよ．

from test67 import *

def main():
	vectors_dict = pickle.load(open("test66_np_vectors.pkl","r")) #test66の各ベクトルを格納したもの
	all_nps = [np for np in vectors_dict.keys()]

	similarities = {}
	
	i = 0
	for np1 in all_nps:
		i += 1
		for np2 in all_nps[i:]:
			similarities["\t".join([np1, np2])] = cos_similarity(vectors_dict,np1,np2)

	for k,v in sorted(similarities.items(), key=lambda x:x[1], reverse=True):
		if v > 0.6:
			print "%s\t%s"%(v,k)


if __name__ == '__main__':
	main()