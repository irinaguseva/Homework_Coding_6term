from googletrans import Translator, LANGUAGES

def lang_table():
    print('-'*33)
    for code in LANGUAGES:
        print('|', LANGUAGES[code] + ' '*(22-len(LANGUAGES[code])) + '| ' + code + ' '*(6-len(code)) + '|')
    print('-'*33)

def user_text_input():
    return input('Write down the text you want to translate: ')

def table_text():
    print('The table above contains supported languages and their codes.')

def get_src_language():
    return input('Source language code: ')
    
def get_dst_language():
    return input('Destination language code: ')
    
def output(translated_text):
    print()
    print('Your results: ')
    print('Initial text: ', translated_text.origin)
    print()
    print('Translated text: ', translated_text.text)
    print()
