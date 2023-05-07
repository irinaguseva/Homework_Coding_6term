import re

text = [" my heart in the higlands",
        "my heart isn't here ",
        "",
        "   ",
        " my heart in the highlands a'chasing the deer "
        ]

for i in range(len(text)):
    text[i] = re.sub('^\s+|\s+$', '', text[i])

text = list(filter(None, text))
print(text)
