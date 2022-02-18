def open_words_file_to_list(file_name):
    l = None
    with open(file_name, 'r', encoding="utf-8") as f:
        l = f.read().split('\n')
    valid_lines = []
    for line in l:
        t = line.strip()
        if not t or t[0] == '#':
            continue
        valid_lines.append(t)
    sedy_words = []
    for line in valid_lines:
        eng_word, *sedy_chars = line.replace(',', ' ').split()
        sedy_words.append((sedy_chars, eng_word))
    return sedy_words
