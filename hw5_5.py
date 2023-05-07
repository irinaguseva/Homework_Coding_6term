import re

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.tokens = []

    def tokenize(self):
        punctuation = r'\W+'
        cyrillic_word = r'[а-яА-Я]+'
        latin_word = r'[a-zA-Z]+'

        for word in re.findall(r'\w+|\W+', self.text):
            if re.match(punctuation, word):
                self.tokens.append(('punctuation', word))
            elif re.match(cyrillic_word, word):
                self.tokens.append(('cyrillic', word))
            elif re.match(latin_word, word):
                self.tokens.append(('latin', word))
        return self.tokens
    
text = "Привет, мир! Why? do! you cry/"
tokenizer = Tokenizer(text)
for item in tokenizer.tokenize():
    print(item[1], item[0])