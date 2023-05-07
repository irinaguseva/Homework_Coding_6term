import re

text = ['Я к вам 4.678 пишу — чего же боле?',
        'Что я могу еще 5,123 сказать?',
        'Теперь, 676 я знаю, в вашей воле',
        'Меня презреньем 9.5 наказать.',
        '88888.88888888',
        'нагореарарат7,999рвалаварваравиноград',
        'В большом 4.569 ауле 7.109 под горою 4.569'
        ]

for i in range(len(text)):
    matches = re.findall('\d*[.,]\d+', text[i])
    
    for match in matches:
        replaced = match.replace(',', '.')
        rounded = round(float(replaced), 2)
        if replaced != match:
            rounded = str(rounded).replace('.', ',')
        text[i] = text[i].replace(match, str(rounded))
        
    print(text[i])
