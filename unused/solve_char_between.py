################################

# tableが手に入ったためそれを参考にして作る
# 今後このプログラムは使わないだろう

################################

# eng -> english
# sedy -> in game language


WORDS_FILE_NAME = "words.txt"
# WORDS_FILE_NAME = "words_red.txt"
# WORDS_FILE_NAME = "words_noloop.txt"
# WORDS_FILE_NAME = "words_playground.txt"
# WORDS_FILE_NAME = "words_tutorial.txt"

INF = 10**18

def num_to_eng_char(num):
    return chr(ord('a')+num)
def nums_to_eng_word(nums):
    return ''.join(map(num_to_eng_char, nums))
all_eng_chars = nums_to_eng_word(range(26))
all_sedy_chars = """
clover
squ
rectface
para
xrect
door
bullet
three
sand
banner
cd
wani
fly
chicken
iron
v
a
triface
back
flag
anemone
wifi
grave
slash
mag
revface
""".strip().split()

def print32(s=""):
    print(s+'='*max(0, 32-len(s)))


with open(WORDS_FILE_NAME, 'r', encoding='utf-8') as f:
    word_texts = f.read().split('\n')

print32()
sedy_char_inword_cnt = 0
graph = dict()
for t in word_texts:
    t = t.strip()
    if not t or t[0] == '#':
        continue
    eng_chars, sedy_chars_text = t.split()
    sedy_chars = sedy_chars_text.split(',')
    sedy_char_inword_cnt += len(sedy_chars)
    sedy_char_idxs = set(zip(sedy_chars, map(ord, eng_chars)))
    for sedy_c1, idx1 in sedy_char_idxs:
        for sedy_c2, idx2 in sedy_char_idxs:
            ### "z"->"a" OK
            # 本来26のあまりになるべきだがゲーム作者のミスで25のあまりとなっている
            d = (idx2-idx1)%26
            # d = (idx2-idx1)%25
            if sedy_c1 not in graph:
                graph[sedy_c1] = dict()
            if sedy_c2 in graph[sedy_c1]:
                if graph[sedy_c1][sedy_c2] != d:
                    print("error: MUJUN")
                    print(f"{eng_chars}: {sedy_c1} => {sedy_c2}: {graph[sedy_c1][sedy_c2]}/{d}")
            else:
                graph[sedy_c1][sedy_c2] = d
            ### "z"->"a" NG
            # d = (idx2-idx1)
            # if sedy_c1 not in graph:
            #     graph[sedy_c1] = dict()
            # if sedy_c2 in graph[sedy_c1]:
            #     if graph[sedy_c1][sedy_c2] != d:
            #         print("error: MUJUN")
            #         print(f"{eng_chars}: {sedy_c1} => {sedy_c2}: {graph[sedy_c1][sedy_c2]}/{d}")
            # else:
            #     graph[sedy_c1][sedy_c2] = d
print32()

print32()
non_sedy_chars = [c for c in graph.keys() if c not in all_sedy_chars]
if non_sedy_chars:
    print("error: words.txt includes non sedy character.")
    print(f"non sedy characters: {non_sedy_chars}")
    exit()
non_exist_chars = [c for c in all_sedy_chars if c not in graph.keys()]
print(f"non exist characters: {non_exist_chars}")
print32()


print32()
dist = dict(zip(graph.keys(), [INF]*len(graph)))
def solve_dist_from(start):
    dist[start] = 0
    q = [start]
    group_nodes = []
    while q:
        t = q.pop()
        group_nodes.append(t)

        for to, cost in graph[t].items():
            ### "z"->"a" OK
            to_dist = (dist[t] + cost)%26
            if dist[to] != INF:
                if dist[to] != to_dist:
                    print("error: MUJUN II")
                    print(f"{t} -> {to}: {dist[to]}/{to_dist}")
                continue
            dist[to] = to_dist
            q.append(to)
            ### "z"->"a" NG
            # to_dist = (dist[t] + cost)
            # if not (0 <= to_dist < 26):
            #     continue
            # if dist[to] != INF:
            #     if dist[to] != to_dist:
            #         print("error: MUJUN")
            #         print(f"{t} -> {to}: {dist[to]}/{to_dist}")
            #     continue
            # dist[to] = to_dist
            # q.append(to)

    return group_nodes
# 連結成分 list
groups = []
for sedy_char in sorted(graph.keys()):
    if dist[sedy_char] != INF:
        continue
    dist[sedy_char] = 0
    group_nodes = solve_dist_from(sedy_char)
    groups.append(group_nodes)

# for k in ["back", "mag"]:
#     print(k, graph[k])
#     print(dist[k])
# print(dist)

# print32()


def suggest_eng_26patterns_1group(sedy_chars):
    if len(groups) != 1:
        print("error: length of groups is not 1.")
        return
    group = groups[0]
    leader = group[0]
    sedy_char_dists = [dist[sedy_c] for sedy_c in sedy_chars]
    ans = []
    nums = sedy_char_dists
    for i in range(26):
        nums_i = [(num+i)%26 for num in nums]
        eng_word_pattern = nums_to_eng_word(nums_i)
        ans.append(eng_word_pattern)
    ans.sort()
    print(len(ans))
    return ans

def io_info():
    print32("info:")
    # ノード数
    res_node_cnt = len(graph)
    print(f"number of nodes: {res_node_cnt}")
    # 連結成分の個数
    res_group_cnt = len(groups)
    print(f"number of groups {res_group_cnt}")
    # 辞書のsedy文字数
    print(f"number of charactersin dictionaly: {sedy_char_inword_cnt}")
    # 具体的なsedy文字同士の距離
    for g in groups:
        t = ['#']*26
        for gi in g:
            # print(gi, dist[gi])
            t[dist[gi]] = gi
        # t_rev = t[::-1]
        # while t_rev[-1] == '#':
        #     t_rev.pop()
        # t = t_rev[::-1]
        # while t[-1] == '#':
        #     t.pop()
        print('-'*10)
        print(*t, sep='\n')
    print32()

def io_suggest_eng_26patterns():
    print32("suggest_eng_26patterns:")
    input_words = input().replace(',', ' ').split()
    invalid_words = [w for w in input_words if w not in graph]
    if invalid_words:
        print("error: Your input includes invalid or unregistered sedy char.")
        print("invalid words:", ", ".join(invalid_words))
        print32()
        return
    sedy_chars = input_words
    patterns_in_group = suggest_eng_26patterns_1group(sedy_chars)
    print(*patterns_in_group, sep='\n')
    print32()

io_info()
io_suggest_eng_26patterns()