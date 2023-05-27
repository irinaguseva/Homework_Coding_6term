import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from razdel import tokenize

#####################################

en_tokenizer = RegexpTokenizer(r'\w+')
with open('magi_eng.txt', 'r') as f:
    en_raw_text = f.read()
en_sentenized_text = sent_tokenize(en_raw_text)
en_count_sents = len(en_sentenized_text)
print(f"Количество предложений в англоязычном тексте: {en_count_sents}")

en_words = en_tokenizer.tokenize(en_raw_text)
#print(en_words)
count_en_words_in_sentence = len(en_words) / en_count_sents
print(f"Средняя длина предложения в англоязычном тексте: {count_en_words_in_sentence}")

for i in range(len(en_words)):
    en_words[i] = en_words[i].lower()
count_en_words = len(en_words)
count_en_unique_words = len(list(set(en_words)))
print(f"Количество слов в англоязычном тексте - {count_en_words},  уникальных - {count_en_unique_words}")
print(f"Соотношение всех русских слов к уникальным составляет {count_en_words / count_en_unique_words}")

en_tokens_with_punc = [t.text for t in tokenize(en_raw_text)]
en_punc = 0
for t in en_tokens_with_punc:
    if not t.isalnum():
        en_punc += 1

print(f"Соотношение знаков пунктуации и слов в англоязычном тексте составляет {en_punc} / {count_en_words} = {en_punc / count_en_words}")


#####################################

with open('magi_ru.txt', 'r') as f:
    ru_raw_text = f.read()
ru_sentenized_text = sent_tokenize(ru_raw_text)
ru_count_sents = len(ru_sentenized_text)
print(f"Количество предложений в русскоязычном тексте: {ru_count_sents}")

ru_words = re.sub(r'[^\w\s]', '', ru_raw_text)
ru_words = word_tokenize(ru_words, language='russian')
count_ru_words_in_sentence = len(ru_words) / ru_count_sents
print(f"Средняя длина предложения в русскоязычном тексте: {count_ru_words_in_sentence}")

for i in range(len(ru_words)):
    ru_words[i] = ru_words[i].lower()
count_ru_words = len(ru_words)
count_ru_unique_words = len(list(set(ru_words)))
print(f"Количество слов в русскоязычном тексте - {count_ru_words},  уникальных - {count_ru_unique_words}")
print(f"Соотношение всех русских слов к уникальным составляет {count_ru_words / count_ru_unique_words}")

ru_tokens_with_punc = [t.text for t in tokenize(ru_raw_text)] 
ru_punc = 0
for t in ru_tokens_with_punc:
    if not t.isalnum():
        ru_punc += 1
print(f"Соотношение знаков пунктуации и слов в русскоязычном тексте составляет {ru_punc} / {count_ru_words} = {ru_punc / count_ru_words}")


######################################

# Количество предложений в англоязычном тексте: 141
# Средняя длина предложения в англоязычном тексте: 15.063829787234043
# Количество слов в англоязычном тексте - 2124,  уникальных - 756
# Соотношение всех русских слов к уникальным составляет 2.8095238095238093
# Соотношение знаков пунктуации и слов в англоязычном тексте составляет 401 / 2124 = 0.18879472693032015

# Количество предложений в русскоязычном тексте: 161
# Средняя длина предложения в русскоязычном тексте: 11.15527950310559
# Количество слов в русскоязычном тексте - 1796,  уникальных - 1003
# Соотношение всех русских слов к уникальным составляет 1.7906281156530408
# Соотношение знаков пунктуации и слов в русскоязычном тексте составляет 448 / 1796 = 0.24944320712694878
