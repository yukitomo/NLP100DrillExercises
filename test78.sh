#(78) 学習したモデルmodel.txtを使い，data00.fの素性から冠詞のタイプを予測せよ．このとき，予測された冠詞のタイプと，正解の冠詞のタイプを並べて出力せよ．
cat sec8_english_texts/english_1.f | classias-tag -m test77_model.txt -r > test78_output.txt