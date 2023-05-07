import re

text = [" my heart in the higlands",
        "my heart isn't here ",
        "",
        "   ",
        " my heart in the highlands a'chasing the deer "
        ]
i = 0
while i < len(text):
    text[i] = re.sub('^\s+|\s+$', '', text[i])
    if text[i]:
        print(text[i])
        i += 1
    else:
        del text[i]

