from encodings import utf_8
from yayoutils import *

WORDS_FILE_NAME = "words_wrong_loop.txt"
TABLE_FILE_NAME = "table_from_hidden_door.txt"

all_sedy_chars = None
with open(TABLE_FILE_NAME, 'r', encoding="utf-8") as f:
    all_sedy_chars = f.read().split('\n')

to_num_dict = dict(zip(all_sedy_chars, range(26)))
to_num = lambda x: to_num_dict[x]
to_sedy_char = lambda x: all_sedy_chars[x]
to_eng_char = lambda x: chr(ord('a')+x)

def suggest_eng_26pattern_with_table(sedy_chars):
    sedy_idxs = list(map(to_num, sedy_chars))
    patterns = []
    for i in range(26):
        # correct
        # idxs_i = [(x+i)%26 for x in sedy_idxs]
        # idxs_i = [(x-i)%26 for x in sedy_idxs]
        # wrong loop 製作者のミス
        idxs_i = [(x-i)%25 for x in sedy_idxs]
        p = ''.join(map(to_eng_char, idxs_i))
        patterns.append(p)
    return patterns

def io_suggest_eng_26pattern_with_table():
    words = input().replace(',', ' ').split()
    invalids = [w for w in words if w not in all_sedy_chars]
    if invalids:
        print("error:")
        print(f"invalids: {invalids}")
        return
    sedy_chars = words
    patterns = suggest_eng_26pattern_with_table(sedy_chars)
    # for i in range(-13, 13):
    #     print(f"{i: >4}: {patterns[i]}")
    for p in patterns:
        print(p)

def check_words_file(file_name):
    words = open_words_file_to_list(file_name)
    for sedys, eng_word in words:
        patterns = suggest_eng_26pattern_with_table(sedys)
        if eng_word in patterns:
            pass
        else:
            print("suggest is missed.")
            print("f{eng_word}")
            print(*patterns, sep='\n')

if __name__ == "__main__":
    io_suggest_eng_26pattern_with_table()
# check_words_file(WORDS_FILE_NAME)