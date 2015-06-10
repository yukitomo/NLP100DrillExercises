#!/usr/bin/python
#-*-coding:utf-8-*-
#(4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．

def make_list(f):
	list = []
	for line in f:
		list.append(line.strip())
	return list 

def main():
	f1=open('col1.txt','r')
	f2=open('col2.txt','r')
	list1 = make_list(f1)
	list2 = make_list(f2)

	for i in range(len(list1)):
		print list1[i] + "\t" +  list2[i] 

if __name__ == '__main__':
	main()