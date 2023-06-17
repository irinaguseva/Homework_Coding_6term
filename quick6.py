import spacy
import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

nlp = spacy.load("en_core_web_sm")

with open('magi_eng.txt', 'r', encoding='utf-8', errors='ignore') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
dic_eng = {}
for sent in en_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Upos = token.pos_
    if Upos not in dic_eng:
      dic_eng[Upos] = 1
    else:
      dic_eng[Upos] += 1

!python3 -m spacy download ru_core_news_md

with open('magi_ru.txt', 'r', encoding='utf-8', errors='ignore') as f:
  ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
dic_ru = {}
for sent in ru_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Upos = token.pos_
    if Upos not in dic_ru:
      dic_ru[Upos] = 1
    else:
      dic_ru[Upos] += 1


tot_eng = sum(dic_eng.values())
tot_ru = sum(dic_ru.values())

sorted_dic_eng = sorted(dic_eng.items(), key = lambda x : -x[1])

print(f"{'POS':5} {'English':5} {'Russian':5}")
print()
for item in sorted_dic_eng:
    x_eng = round((item[1] / tot_eng)*100, 2)
    x_ru = round((dic_ru[item[0]] / tot_ru)*100, 2)
    print(f"{item[0]:5} {x_eng:5}% {x_ru:5}%")


######################################################

# POS   English Russian

# NOUN  14.68%  17.7%
# PUNCT 14.23% 19.29%
# VERB  11.45% 12.96%
# PRON  11.37%  7.04%
# ADP   10.12%   8.5%
# DET    8.63%  2.52%
# ADJ    5.73%   7.7%
# AUX     5.2%  1.15%
# ADV    5.08%  7.57%
# CCONJ  4.15%  4.51%
# PROPN  3.95%  4.38%
# PART   1.85%  3.41%
# NUM    1.69%  1.55%
# SCONJ  1.37%  1.59%
# SYM    0.24%   0.0%
# INTJ   0.24%  0.04%
# SPACE   0.0%  0.09%
