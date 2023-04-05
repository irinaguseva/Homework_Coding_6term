import re

file = input()

with open(file, 'r', encoding='utf8') as f:
    f = f.readlines()

counter = 0
for line in f:
    
    counter += 1
    
    line = line.rstrip('\n')
    line = re.sub(r'[^\w\s]', '', line)
    line = line.split()

    for word in line:
        if not (re.match(r'^[a-zA-Z]+$', word) or re.match(r'^[а-яА-Я]+$', word)):
            listy = re.findall(r'[a-zA-Z]', word)
            print(f'Line {counter}. Token "{word}" contains cyrillic and latin characters: {listy}')