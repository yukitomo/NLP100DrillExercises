#!/user/bin/python
#-*-coding:utf-8-*-
#(45) 文章中の「ＡのＢ」という表現（ＡとＢは名詞の１形態素）をすべて抜き出せ．

import pickle

def AnoB_extractor(text):
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["surface"]=="の":
				if text[m][n-1]["pos"]=="名詞" and text[m][n+1]["pos"]=="名詞":
					print text[m][n-1]["surface"]+text[m][n]["surface"]+text[m][n+1]["surface"]+"\n",
				else:pass
			else:pass

def main():
	text = pickle.load(open("test41_output.pickle","r"))
	AnoB_extractor(text)

if __name__ == '__main__':
	main()

