from yayoutils import *

enum = enumerate
WORDS_FILE_NAME = "words_all.txt"

# 元凶である
# todo.md 法則の解析 を参照してください
def calc_eng_char_dist(a, b):
    x = ord(b) - ord(a)
    if x < 0:
        x %= 25
    return x

words = open_words_file_to_list(WORDS_FILE_NAME)

word_inword_dists = dict()
for sedy_chars, eng_word in words:
    ziped_chars = list(zip(sedy_chars, eng_word))
    inword_dist = dict()
    for i, (sc1, ec1) in enum(ziped_chars):
        for j, (sc2, ec2) in enum(ziped_chars):
            if i == j:
                continue
            dist = calc_eng_char_dist(ec1, ec2)
            inword_dist[(sc1, sc2)] = dist
    word_inword_dists[eng_word] = inword_dist

tmp = word_inword_dists.items()
for ak, av in tmp:
    for bk, bv in tmp:
        if ak == bk:
            continue
        both_set = set(av) & set(bv)
        for x_to_y in both_set:
            if av[x_to_y] == bv[x_to_y]:
                # print(ak, bk, x_to_y, f"dist: {av[x_to_y]}")
                pass
            else:
                print("ERROR: MUJUN")
                print(f"{ak}, {bk}: {x_to_y} = {av[x_to_y]}/{bv[x_to_y]}")
