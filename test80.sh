#-*-coding:utf-8-*-
echo imput_sent
read line
cd /Users/shin/work/nlp100knock/geniatagger-3.0.1/
#export PATH=$PATH:/Users/shin/work/nlp100knock/geniatagger-3.0.1/
word=`echo $line | ./geniatagger `
echo $word
cd /Users/shin/git/NLP100knock
python test080.py $word
cat 80_output_genear_noun.f
cat 80_output_genear_noun.f | classias-tag -m 77.model -r > 80_output_classias.txt
cat 80_output_classias.txt
python test080_compere.py 80_output_classias.txt $word