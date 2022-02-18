from base64 import decode
from fileinput import filename
from yayoutils import *
from solve_with_table import suggest_eng_26pattern_with_table

WORDS_FILE_NAME = "words_news.txt"
NEWS_FILE_NAME = "news_1.txt"

l = open_words_file_to_list(WORDS_FILE_NAME)
d = dict((tuple(s), e) for s, e in l)

def add_word(sedys, eng_word):
    sedys = tuple(sedys)
    if sedys in d:
        return False
    d[sedys] = eng_word
    is_newlined = None
    with open(WORDS_FILE_NAME, 'r', encoding="utf-8") as f:
        is_newlined = f.read()[-1] == '\n'
    with open(WORDS_FILE_NAME, 'a', encoding="utf-8") as f:
        if not is_newlined:
            f.write('\n')
        t = f"{eng_word} {','.join(sedys)}\n"
        f.write(t)
    return True

def io_suggest_sedys_to_eng(sedys):
    patterns = suggest_eng_26pattern_with_table(sedys)
    print(f"[{','.join(sedys)}]")
    for i, p in enumerate(patterns):
        print(f"{i: >3}: {p}")
    while True:
        in_text = input()
        if not in_text:
            continue
        if not all('0' <= c <= '9' for c in in_text):
            continue
        if not (0 <= int(in_text) <= 26):
            continue
        break
    num = int(in_text)
    if num == 26:
        return "?"*len(sedys) 
    else:
        return patterns[num]

def decode_sedys_to_eng(sedys):
    sedys = tuple(sedys)
    if sedys in d: # and d[sedys] != "???" 
        pass
    else:
        print()
        eng_word = io_suggest_sedys_to_eng(sedys)
        add_word(sedys, eng_word)
    return d[sedys]

def read_file_to_sedys_list(file_name):
    sedys_list = None
    with open(file_name, 'r', encoding='utf-8') as f:
        sedys_list = [s.split(',') for s in f.read().split()]
    return sedys_list

sedys_list = read_file_to_sedys_list(NEWS_FILE_NAME)

# print(sedys_list)
for sedys in sedys_list:
    ans = decode_sedys_to_eng(sedys)
    print(ans, end=' ')
