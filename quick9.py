import spacy
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

###########   ENGLISH   #############

nlp = spacy.load("en_core_web_sm")
with open('magi_eng.txt', 'r', encoding='utf-8', errors='ignore') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
dep_dic_eng = {}
for sent in en_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Deprel = token.dep_
    if Deprel not in dep_dic_eng:
      dep_dic_eng[Deprel] = {}
    if token.text.lower() not in dep_dic_eng[Deprel]:
      dep_dic_eng[Deprel][token.text.lower()] = 1
    else:
      dep_dic_eng[Deprel][token.text.lower()] += 1

for dep in dep_dic_eng:
  lst = sorted(dep_dic_eng[dep].items(), key = lambda x : -x[1])
  print(f"The most frequent tokens for {dep}:")
  if len(lst) >= 3:
    leng = 3
  else:
    leng = len(lst)
  for i in range(leng):
    print(lst[i][0], lst[i][1], sep=' ')
  print()


# The most frequent tokens for nummod:
# one 4
# two 4
# twenty 3

# The most frequent tokens for ROOT:
# was 15
# said 9
# looked 6

# The most frequent tokens for cc:
# and 83
# but 11
# or 5

# The most frequent tokens for compound:
# james 4
# dillingham 4
# christmas 4

# The most frequent tokens for punct:
# . 142
# , 104
# “ 30

# The most frequent tokens for conj:
# was 5
# let 3
# cents 2

# The most frequent tokens for nsubj:
# she 32
# i 18
# he 16

# The most frequent tokens for attr:
# all 1
# christmas 1
# nothing 1

# The most frequent tokens for prep:
# of 47
# in 24
# with 21

# The most frequent tokens for pobj:
# it 7
# you 5
# me 5

# The most frequent tokens for dobj:
# it 14
# present 4
# hair 4

# The most frequent tokens for det:
# the 116
# a 65
# that 6

# The most frequent tokens for pcomp:
# giving 2
# bulldozing 1
# predominating 1

# The most frequent tokens for amod:
# beautiful 5
# brown 4
# little 3

# The most frequent tokens for poss:
# her 21
# his 18
# my 8

# The most frequent tokens for case:
# ’s 6

# The most frequent tokens for acl:
# burned 1
# bearing 1
# walking 1

# The most frequent tokens for mark:
# as 7
# that 6
# if 3

# The most frequent tokens for relcl:
# buy 3
# made 2
# took 2

# The most frequent tokens for npadvmod:
# jim 3
# times 2
# week 2

# The most frequent tokens for aux:
# to 19
# had 17
# could 7

# The most frequent tokens for expl:
# there 6

# The most frequent tokens for advmod:
# just 8
# now 7
# very 4

# The most frequent tokens for prt:
# out 7
# up 5
# off 5

# The most frequent tokens for nsubjpass:
# it 3
# life 1
# dillingham 1

# The most frequent tokens for auxpass:
# was 4
# been 3
# be 3

# The most frequent tokens for advcl:
# being 2
# lived 2
# subsiding 1

# The most frequent tokens for nmod:
# $ 4
# dollar 1

# The most frequent tokens for neg:
# n’t 12
# not 7
# never 1

# The most frequent tokens for csubj:
# appertaining 1

# The most frequent tokens for acomp:
# good 2
# worthy 2
# wisest 2

# The most frequent tokens for oprd:
# jim 1
# while 1

# The most frequent tokens for agent:
# by 3

# The most frequent tokens for dep:
# all 1
# read 1

# The most frequent tokens for quantmod:
# $ 2
# a 2

# The most frequent tokens for xcomp:
# look 2
# planning 1
# depreciate 1

# The most frequent tokens for appos:
# jim 2
# something 1
# both 1

# The most frequent tokens for ccomp:
# look 3
# buy 2
# be 2

# The most frequent tokens for predet:
# all 2

# The most frequent tokens for meta:
# dollars 1
# dell 1

# The most frequent tokens for dative:
# to 2
# for 2
# you 2

# The most frequent tokens for intj:
# oh 4
# please 1

# The most frequent tokens for parataxis:
# cried 1
# mind 1
# knew 1

###########   RUSSIAN   #############

!python3 -m spacy download ru_core_news_md
nlp = spacy.load('ru_core_news_md')
with open('magi_ru.txt', 'r', encoding='utf-8', errors='ignore') as f:
    ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
dep_dic_ru = {}
for sent in ru_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Deprel = token.dep_
    if Deprel not in dep_dic_ru:
      dep_dic_ru[Deprel] = {}
    if token.text.lower() not in dep_dic_ru[Deprel]:
      dep_dic_ru[Deprel][token.text.lower()] = 1
    else:
      dep_dic_ru[Deprel][token.text.lower()] += 1

for dep in dep_dic_ru:
  lst = sorted(dep_dic_ru[dep].items(), key = lambda x : -x[1])
  print(f"The most frequent tokens for {dep}:")
  if len(lst) >= 3:
    leng = 3
  else:
    leng = len(lst)
  for i in range(leng):
    print(lst[i][0], lst[i][1], sep=' ')
  print()


# The most frequent tokens for nummod:
# один 5
# двадцати 1
# семью 1

# The most frequent tokens for ROOT:
# можно 4
# доллар 3
# всё 3

# The most frequent tokens for cc:
# и 68
# а 13
# но 12

# The most frequent tokens for conj:
# восемьдесят 5
# джим 3
# продала 3

# The most frequent tokens for nummod:gov:
# семь 5
# двадцать 4
# восемь 3

# The most frequent tokens for nsubj:
# делла 20
# она 20
# я 14

# The most frequent tokens for punct:
# , 194
# . 144
# — 57

# The most frequent tokens for acl:relcl:
# удалось 1
# смог 1
# возвращался 1

# The most frequent tokens for csubj:
# жарить 2
# отложить 1
# торговаться 1

# The most frequent tokens for case:
# в 43
# на 34
# из 15

# The most frequent tokens for obl:
# меня 5
# них 3
# долларов 3

# The most frequent tokens for amod:
# радостный 3
# потёртый 2
# сам 2

# The most frequent tokens for det:
# его 3
# её 3
# все 3

# The most frequent tokens for mark:
# что 6
# как 5
# словно 4

# The most frequent tokens for fixed:
# что 5
# и 3
# равно 2

# The most frequent tokens for advmod:
# не 30
# же 9
# уже 8

# The most frequent tokens for advcl:
# горели 1
# переходит 1
# получал 1

# The most frequent tokens for nmod:
# неделю 4
# джима 3
# деллы 3

# The most frequent tokens for acl:
# одобрявших 1
# состоит 1
# пустующий 1

# The most frequent tokens for obj:
# их 6
# волосы 5
# её 4

# The most frequent tokens for ccomp:
# оставалось 1
# подарить 1
# достойна 1

# The most frequent tokens for xcomp:
# принадлежать 2
# осмотрим 1
# выжать 1

# The most frequent tokens for aux:
# бы 8
# было 1
# будешь 1

# The most frequent tokens for parataxis:
# сказала 5
# да 3
# джим 2

# The most frequent tokens for appos:
# джеймс 4
# диллингхем 1
# джиму 1

# The most frequent tokens for flat:name:
# диллингхем 4
# янг 4
# джиму 1

# The most frequent tokens for iobj:
# тебе 6
# джиму 5
# вам 3

# The most frequent tokens for cop:
# была 4
# были 3
# будет 2

# The most frequent tokens for orphan:
# раньше 1

# The most frequent tokens for nsubj:pass:
# шляпка 1
# кофе 1
# утверждение 1

# The most frequent tokens for discourse:
# убьёт 1
# господи 1
# волосы 1

# The most frequent tokens for aux:pass:
# был 1

# The most frequent tokens for dep:
#    2


