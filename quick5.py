import spacy
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


###########   ENGLISH   #############

nlp = spacy.load("en_core_web_sm")
with open('magi_eng.txt', 'r', encoding='utf-8', errors='ignore') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
Deps, Misc = '-', '-'
lst = []
for sent in en_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    ID = str(i + 1)
    Word = token.text
    Lemma = token.lemma_
    Upos = token.pos_
    Xpos = token.tag_
    Feat = str(token.morph)
    Deprel = token.dep_
    if Deprel == 'ROOT':
      Deprel = 'root'
      Head = '0'
    else:
      Head = str(token.head.i + 1)
    line = f'{ID:4} {Word:15} {Lemma:15} {Upos:10} {Xpos:10} {Feat:65} {Head:5} {Deprel:10} {Deps:5} {Misc:5}'
    lst.append(line + '\n')
    print(line)

with open('quick5_eng.conllu', 'w') as f:
  f.writelines(lst)

!python3 -m spacy download ru_core_news_md

#############  RUSSIAN   ###############

nlp = spacy.load("ru_core_news_md")
with open('magi_ru.txt', 'r', encoding='utf-8', errors='ignore') as f:
    ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
Deps, Misc = '-', '-'
lst = []
for sent in ru_sentenized_text:
  doc = nlp(sent)
  for i in range(len(doc)):
    token = doc[i]
    ID = str(i + 1)
    Word = token.text
    Lemma = token.lemma_
    Upos = token.pos_
    Xpos = token.tag_
    Feat = str(token.morph)
    Deprel = token.dep_
    if Deprel == 'ROOT':
      Deprel = 'root'
      Head = '0'
    else:
      Head = str(token.head.i + 1)
    line = f'{ID:4} {Word:15} {Lemma:15} {Upos:10} {Xpos:10} {Feat:85} {Head:5} {Deprel:10} {Deps:5} {Misc:5}'
    lst.append(line + '\n')
    print(line)

with open('quick5_ru.conllu', 'w') as f:
  f.writelines(lst)