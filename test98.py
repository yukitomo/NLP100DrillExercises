#!/usr/bin/python
#-*-coding:utf-8-*-
#(98) 現在時刻を表示するCGIを，自分のウェブサイト上で公開せよ．
#cgi-bin/test98.py

#python -m CGIHTTPServer　ディレクトリcgi-binのある場所でローカルサーバーを起動
#chmod 755 test98.py 実行権限を付加
#http://localhost:8000/cgi-bin/test98.py にアクセス

from datetime import datetime

print "Content-Type: text/html; charset=utf-8"
print
print "<h1>"
print datetime.now()
print "</h1>"