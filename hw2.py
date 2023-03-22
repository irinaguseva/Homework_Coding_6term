import wikipediaapi
import json
import time

my_category = "Sorting algorithms"
articles = []

wiki_wiki = wikipediaapi.Wikipedia('en')

def find_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            articles.append(c.title)
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                find_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)

cat = wiki_wiki.page("Category:" + my_category)
find_categorymembers(cat.categorymembers)

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

list_with_data = []
for item in articles:
    p_wiki = wiki_wiki.page(item)
    time.sleep(1)
    dic = {}
    dic[item] = p_wiki.text
    list_with_data.append(dic)

json_data = json.dumps(list_with_data)
print(json_data)

with open("sorting_algorithms.json", 'w') as f:
    json.dump(json_data, f)