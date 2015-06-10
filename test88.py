#!/usr/bin/python
#-*-coding:utf-8-*-
#(88) 81-82の処理に加え，ツイート本文の文字バイグラムをドキュメントに追加し，このフィールドでインデックスを構築せよ．
	#(81) このデータをMongoDBに格納せよ．ただし，MongoDBのデータベース名は"nlp100_{ユーザ名}"，コレクション（テーブル）名は"tweets"とし，ドキュメント（レコード）のフィールドには適当な名前を付けよ．
	#(82) MongoDBの対話型シェルを用い，url, date, user, rt_url, reply_url, qt_urlに対してインデックスを構築せよ．


import pymongo
from pymongo import *


def make_bigram_list(text): #textはユニコード
	bigram_list = []
	for i in range(len(text)-1): #文字バイグラム
		bigram_list.append(text[i:i+2])
	return bigram_list



if __name__ == '__main__':

	con = Connection('YUKITOMO-MBA11.local')

	#コネクションからnlp100_tomoデータベースを取得
	db = con.nlp100_tomo

	#nlp100_tomoデータベースからtweetsコレクションを取得
	col = db.tweets

	for data in col.find():
		bigram_list = make_bigram_list(data["body"])
		print bigram_list
		col.update({"_id":data["_id"]},{"$set":{"bigram":bigram_list}})

		
