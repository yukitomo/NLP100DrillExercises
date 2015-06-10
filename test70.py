#!/usr/bin/python
#-*-coding:utf-8-*-

#(70) 68の結果を用い，最長距離法（furthest neighbor method; complete link method）で名詞句のクラスタリングを行い，クラスタを抽出せよ．

import sys
from collections import defaultdict


def getClassSimilarity(c1, c2):

    # クラスの要素間での類似度計算(総当り)
    # その全ての類似度をリストに格納後、後でminimumを返す(最長距離法のため)
    # 内積辞書はdefaultで1.0なのでそもそも内積が存在しない場合は1.0になる
    # (最長距離法なので、1.0はどうせ無視される)
    # もし全ての要素の類似度が1.0なら(min=1.0, 全パターンやってもひとつも内積が存在しないなら)クラス間類似度は0にする
    
    similar_list = []
    for c1_item in c1:
        for c2_item in c2:
            similar_list.append(product_dict[c1_item+"\t"+c2_item])
    return min(similar_list) if min(similar_list) != 1 else 0


def main():
    similarities_scores = defaultdict(lambda: 1.0)
    stop_number = int(raw_input("input stop number"))

    for line in open("test68_output.txt","r"):
        line = line.strip().split("\t")
        score = float(line[0])
        noun1 = line[1]
        noun2 = line[2]
        class_list.append(noun1)
        class_list.append(noun2)
        similarities_scores[noun1+"\t"+noun2] = score
        similarities_scores[noun2+"\t"+noun1] = score

    class_list = [[noun] for noun in set(class_list)]

    #furthest neighbor method; complete link method

    while len(class_list) > stop_number:
        best_similarrity = .0
        neighbor_class = ()
        # クラスを総当りで類似度を計算して。一番高いものをマージする
        # 計算量を下げるためにネストされてるループは開始位置を変えてる
        # O(n*n) -> O(n*logn)
        for class1, i in zip(class_list, range(len(class_list))):
            for class2 in class_list[i+1:]:
                new_similarrity = getClassSimilarity(class1, class2)
                if best_similarrity < new_similarrity:
                    neighbor_class = (class1, class2)
                    best_similarrity = new_similarrity
        # 総当りしても一番いい類似度が0ってことは、もう内積辞書での組み合わせがない
        if best_similarrity == 0:
            print "can not merge anymore!"
            break
        class_list.append(neighbor_class[0]+neighbor_class[1])
        class_list.remove(neighbor_class[0])
        class_list.remove(neighbor_class[1])

    # 出力
    for one_class, i in zip(class_list, range(len(class_list))):
        print "class :", i+1, ",".join(one_class)



if __name__ == '__main__':
    main()