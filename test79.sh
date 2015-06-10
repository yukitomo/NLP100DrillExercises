#(79) data00.f～data04.fを用いて５分割交差検定を行い，冠詞予測の精度，適合率，再現率，F1スコアを求めよ．
classias-train -tm  -g5 -x sec8_english_texts/english_1.f sec8_english_texts/english_2.f sec8_english_texts/english_3.f sec8_english_texts/english_4.f sec8_english_texts/english_5.f


#result
#***** Iteration #123 *****
#Loss: 4198.79
#Feature L2-norm: 37.5767
#Error norm: 1.76726
#Active features: 109592 / 126220
#Line search trials: 1
#Line search step: 1
#Seconds required for this iteration: 0.02
#Accuracy: 0.8657 (3295/3806)
#Micro P, R, F1: 0.8657 (3295/3806), 0.8657 (3295/3806), 0.8657
#Macro P, R, F1: 0.8000, 0.5835, 0.6245

#L-BFGS terminated with the stopping criteria
#Seconds required: 2.01

#Finish time: 2015-01-14T08:21:26Z
