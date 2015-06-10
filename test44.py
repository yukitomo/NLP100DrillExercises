#!/user/bin/python
#-*-coding:utf-8-*-
#(44) サ変名詞をすべて抜き出せ．
"""
>>> print m.parse("(掃除)")
(	名詞,サ変接続,*,*,*,*,*
掃除	名詞,サ変接続,*,*,*,*,掃除,ソウジ,ソージ
)	名詞,サ変接続,*,*,*,*,*
"""

import pickle

def noun_sahenn_extractor(text):
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["pos"]=="名詞" and text[m][n]["pos1"]=="サ変接続":
				#print text[m][n]["surface"]+"\t"+text[m][n]["base"]
				print text[m][n]["surface"]

def main():
	text = pickle.load(open("test41_output.pickle","r"))
	noun_sahenn_extractor(text)

if __name__ == '__main__':
	main()

