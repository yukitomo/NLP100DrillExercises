#!/usr/bin/python
#-*-coding:utf-8-*-
#(81) このデータをMongoDBに格納せよ．ただし，MongoDBのデータベース名は"nlp100_{ユーザ名}"，コレクション（テーブル）名は"tweets"とし，ドキュメント（レコード）のフィールドには適当な名前を付けよ．

"""
mongod --dbpath ./set9_db
新しくターミナルを開く
mongo
s
db 今使っているdbを表示
show dbs　すべてのdbを表示
db.tweets.find() 

db.dropDatabase() データベースの削除

http://gihyo.jp/dev/serial/01/mongodb/0001?page=3

mongoDBの終了　
exit
http://mironal-memo.blogspot.jp/2012/07/mongodbrunexit.html

pymongo
https://github.com/mongodb/mongo-python-driver
http://kesin.hatenablog.com/entry/2013/11/15/Python%E3%81%A7MongoDB%E3%82%92%E4%BD%BF%E3%81%86unittest%E3%81%AE%E3%81%B2%E3%81%AA%E5%BD%A2

http://www.tkd55.net/blog/?p=732
db.tweets.find({“freq_rted”:{$gt1}})
db.tweets.update({"user" : "bontanname2"},{ $inc:{"freq_rted" : 1}}) 要素のアップデート
db.tweets.find({"freq_rted":{$gt:0}}).sort({"freq_rted":1})

インデックスの作成
db.tweets.ensureIndex({"url":1,"date":1,"user”:1,”freq_rted”:1,”reply_url”:1,”body”:1,”nickname”:1})


"""

from pymongo import Connection
import json
import sys

f = open(sys.argv[1]) 
data = json.load(f)

#コネクション作成
con = Connection('localhost')
#コネクションからtestデータベースを取得
db = con.nlp100_tomo
#testデータベースからfooコレクションを取得
col = db.tweets

for i in data:
	#print i
	url = "https://twitter.com/"+i["user"]["screen_name"]+"/status/"+str(i["id"])
	#print i["in_reply_to_screen_name"],"in_reply_to_screen_name"
	#print i["in_reply_to_status_id"],"in_reply_to_status_id"
	if i["in_reply_to_screen_name"] is None:
		reply_url = None	
	else:
		reply_url = "https://twitter.com/"+i["in_reply_to_screen_name"]+"/status/"+str(i["in_reply_to_status_id"])
	input_data = {"url":url, \
	"date":i["created_at"],\
	"user":i["user"]["screen_name"],\
	"nickname":i["user"]["name"],\
	"body":i["text"],\
	"reply_url":reply_url,\
	"freq_rted":int(i["retweet_count"])\
	}
	col.insert(input_data)