#!/bin/sh
#(61) コーパスディレクトリ中の各ファイルに対して，cabochaを適用し，適当なディレクトリに係り受け解析の結果を格納せよ．ただし，各ファイルの文字コードがUTF-16LEであること，文区切りを自前で行う必要があることに注意せよ．

a=0
while [ $a -lt 5 ];do
a=`expr $a + 1`
cabocha -f1 ./corpus/japanese_${a}.txt > ./work/ja_${a}_cabocha.txt
done


