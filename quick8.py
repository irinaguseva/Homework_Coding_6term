import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'She held it out to him eagerly upon her open palm')
displacy.render(doc, style='dep', jupyter=True, options={'distance': 95})

!python3 -m spacy download ru_core_news_md
nlp = spacy.load('ru_core_news_md')
doc = nlp(u'Она протянула цепочку мужу, держа её на ладони')
displacy.render(doc, style='dep', jupyter=True, options={'distance': 95})
