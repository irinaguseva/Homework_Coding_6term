import spacy
import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

nlp = spacy.load("en_core_web_sm")

with open('magi_eng.txt', 'r', encoding='utf-8', errors='ignore') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
dic_eng = {}
dic_eng_lemma_equals_word = {}
for sent in en_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Word = token.text
    Lemma = token.lemma_
    Upos = token.pos_
    if Word.lower() == Lemma:
      if Upos not in dic_eng_lemma_equals_word:
        dic_eng_lemma_equals_word[Upos] = 1
      else:
        dic_eng_lemma_equals_word[Upos] += 1
    if Upos not in dic_eng:
      dic_eng[Upos] = 1
    else:
      dic_eng[Upos] += 1

!python3 -m spacy download ru_core_news_md

with open('magi_ru.txt', 'r', encoding='utf-8', errors='ignore') as f:
  ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)

nlp = spacy.load("ru_core_news_md")
with open('magi_ru.txt', 'r', encoding='utf-8', errors='ignore') as f:
    ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
dic_ru = {}
dic_ru_lemma_equals_word = {}
for sent in ru_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    Word = token.text
    Lemma = token.lemma_
    Upos = token.pos_
    if Word.lower() == Lemma:
      if Upos not in dic_ru_lemma_equals_word:
        dic_ru_lemma_equals_word[Upos] = 1
      else:
        dic_ru_lemma_equals_word[Upos] += 1
    if Upos not in dic_ru:
      dic_ru[Upos] = 1
    else:
      dic_ru[Upos] += 1

eng_perc = {}
for item in dic_eng_lemma_equals_word:
    eng_perc[item] = round((dic_eng_lemma_equals_word[item]/dic_eng[item]) * 100, 2)
eng_perc = sorted(eng_perc.items(), key = lambda x : -x[1])
print(f"{'POS':7} {'PERCENTAGE':7}")
for item in eng_perc:
    print(f'{item[0]:7} {item[1]:7}%')
print()
ru_perc = {}
for item in dic_ru_lemma_equals_word:
    ru_perc[item] = round((dic_ru_lemma_equals_word[item]/dic_ru[item]) * 100, 2)
ru_perc = sorted(ru_perc.items(), key = lambda x : -x[1])
print(f"{'POS':7} {'PERCENTAGE':7}")
for item in ru_perc:
    print(f'{item[0]:7} {item[1]:7}%')

##########################################
#     ENGLISH
# POS     PERCENTAGE
# NUM       100.0%
# CCONJ     100.0%
# ADP       100.0%
# DET       100.0%
# SCONJ     100.0%
# ADV       100.0%
# SYM       100.0%
# INTJ      100.0%
# ADJ       96.48%
# PRON      82.98%
# PUNCT     82.44%
# NOUN      77.47%
# PART      73.91%
# AUX       40.31%
# VERB      30.99%
# PROPN      1.02%
#     RUSSIAN
# POS     PERCENTAGE
# CCONJ     100.0%
# PART      100.0%
# SPACE     100.0%
# INTJ      100.0%
# ADP        97.4%
# SCONJ     97.22%
# PUNCT     96.79%
# PRON      93.71%
# ADV       89.47%
# NUM       82.86%
# PROPN     82.83%
# AUX       57.69%
# NOUN       41.0%
# DET       31.58%
# VERB      25.94%
# ADJ       23.56%

# Чем больше слов совпадают с леммой, тем менее богата морфология в языке.