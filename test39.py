#!/usr/bin/python
#-*-coding:utf-8-*-
#(39) (38)の出力を読み込み，単語の連接(w, z)をキーとして，その条件付き確率P(z|w)を値とするハッシュデータベースを構築せよ．
#ハッシュデータベースの構築には，Kyoto CabinetのPythonモジュールを用いよ．
#cat test38_output.txt|python test39.py 


#http://d.hatena.ne.jp/ponkotuy/20120105/1325777616
import kyotocabinet as kc
import sys
class KyotoCabinet(kc.DB):
    def __del__(self):
        self.close()

    def open(self, *args, **kwds):
        if not super(KyotoCabinet, self).open(*args, **kwds):
            raise IOError("Open error: {0}".format(super(KyotoCabinet, self).error()))

    def set(self, *args, **kwds):
        if not super(KyotoCabinet, self).set(*args, **kwds):
            raise IOError("Set error: {0}".format(super(KyotoCabinet, self).error()))

    def close(self, *args, **kwds):
        if not super(KyotoCabinet, self).close(*args, **kwds):
            raise IOError("Close error: {0}".format(super(KyotoCabinet, self).error()))

    def cursor(self, *args, **kwds):
        cur = super(KyotoCabinet, self).cursor(*args, **kwds)
        cur.jump()
        while 1:
            rec = cur.get_str(True)
            if not rec: break
            yield rec
        cur.disable()


def main():
    db = KyotoCabinet()
    db.open("test39_db.kch", kc.DB.OWRITER | kc.DB.OCREATE)

    for line in sys.stdin:
        [probability, previous, next] = line.strip().split("\t")
        db.set((previous, next), float(probability))

    for rec in db.cursor():
        print(rec[0], ":", rec[1])

if __name__ == '__main__':
	main()

