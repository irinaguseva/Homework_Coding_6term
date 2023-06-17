import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize

en_tokenizer = RegexpTokenizer(r'\w+')
with open('magi_eng.txt', 'r') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
eng_sent_lens = []
for sentence in en_sentenized_text:
    sentence = en_tokenizer.tokenize(sentence)
    eng_sent_lens.append(len(sentence))
eng_sent_lens.sort()
if len(eng_sent_lens) % 2 == 1:
    med = len(eng_sent_lens)//2
    ans_eng = eng_sent_lens[med]
else:
    med = len(eng_sent_lens)//2
    ans_eng = (eng_sent_lens[med - 1] + eng_sent_lens[med]) / 2
print(f'Медианная длина предложения в англоязычном тексте - {ans_eng}')
#################

with open('magi_ru.txt', 'r') as f:
    ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
ru_sent_lens = []
for sentence in ru_sentenized_text:
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = word_tokenize(sentence, language='russian')
    ru_sent_lens.append(len(sentence))
ru_sent_lens.sort()
if len(ru_sent_lens) % 2 == 1:
    med = len(ru_sent_lens)//2
    ans_ru = ru_sent_lens[med]
else:
    med = len(ru_sent_lens)//2
    ans_ru = (ru_sent_lens[med - 1] + ru_sent_lens[med]) / 2
print(f'Медианная длина предложения в русскоязычном тексте - {ans_ru}')

