#!/usr/bin/python
#-*-coding:utf-8-*-
#(66) 名詞句xの文脈ベクトルを求めよ．ただし，出力形式は"(名詞句i)\t(文脈i_1):(値i_1)\t...(文脈i_m):(値i_m)\n"とせよ
#（ただしmは名詞句iの文脈の種類数）．文脈ベクトルは長さが1になるように正規化しておくとよい．
#我が国 -> する:0.657597 -> いる:0.487923 -> れる:0.146816 <- 年:0.139783 -> 貿易:0.139783 

#cat test65_output.txt |python test66.py

import sys, math, pickle
from collections import defaultdict

def main():
	np_vectors = defaultdict(dict)

	for line in sys.stdin: #test65_output.txt
		line = line.strip().split("\t") #劇場版	->	弾
		np_vectors[line[0]][" ".join(line[1:])] = np_vectors[line[0]].get(" ".join(line[1:]),0) + 1

	#各ベクトルの大きさを計算
	vector_norm = defaultdict(float)
	for np, np_vector in np_vectors.items():
		for ard_word_count in np_vector.values():
			vector_norm[np] += ard_word_count ** 2 
		vector_norm[np] = math.sqrt(vector_norm[np])


	#1に正規化し表示
	for np, np_vector in np_vectors.items():
		print "%s\t"%np,
		for ard_word, ard_word_count in np_vector.items():
			np_vectors[np][ard_word] = ard_word_count / vector_norm[np]
			print "%s:%f\t"%(ard_word, np_vectors[np][ard_word]),
		print ""

	pickle.dump(np_vectors, open("test66_np_vectors.pkl","w"))

if __name__ == '__main__':
	main()
