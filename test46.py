#!/user/bin/python
#-*-coding:utf-8-*-
#(46) 文章中のすべての名詞の連接（１形態素以上）を抜き出せ．

import pickle

def noun_connection_extractor(text):
	mylist=[]
	for m in range(len(text)):
		for n in range(len(text[m])):
			if text[m][n]["pos"]=="名詞":
				mylist.append(text[m][n]["surface"])
			elif len(mylist)>0:
				print " ".join(mylist)
				mylist=[]
			else:pass

def main():
	text = pickle.load(open("test41_output.pickle","r"))
	noun_connection_extractor(text)

if __name__ == '__main__':
	main()


			