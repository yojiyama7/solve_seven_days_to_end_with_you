WORDS_FILE_NAME = "words.txt"
with open(WORDS_FILE_NAME, 'r', encoding='utf-8') as f:
    word_texts = f.read().split('\n')

d = dict()
revd = dict()
for t in word_texts:
    t = t.strip()
    if not t or t[0] == '#':
        continue
    eng_chars, sedy_chars_text = t.split()
    sedy_chars = sedy_chars_text.split(',')
    for ec, sc in zip(eng_chars, sedy_chars):
        if ec not in d:
            d[ec] = dict()
        if sc not in d[ec]:
            d[ec][sc] = 0
        d[ec][sc] += 1
        if sc not in revd:
            revd[sc] = dict()
        if ec not in revd[sc]:
            revd[sc][ec] = 0
        revd[sc][ec] += 1


for k, v in sorted(d.items()):
    print(f"{k}:")
    for vk, vv in sorted(v.items()):
        print(f"  {vk}: {vv}")

print("="*10)

for k, v in sorted(revd.items()):
    print(f"{k}:")
    for vk, vv in sorted(v.items()):
        print(f"  {vk}: {vv}")