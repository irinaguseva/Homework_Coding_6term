from googletrans import Translator
from hw2_2_config import *

user_text = user_text_input()

lang_table()
table_text()

src = get_src_language()
dst = get_dst_language()

translator = Translator()
translated_text = translator.translate(user_text, dest=dst, src=src)

output(translated_text)