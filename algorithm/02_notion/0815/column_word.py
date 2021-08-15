def column_word():
    chars = [input() for _ in range(5)]

    max_len = 0
    for i in range(5):
        if len(chars[i]) > max_len:
            max_len = len(chars[i])

    for j in range(5):
        if len(chars[j]) < max_len:
            chars[j] += '.' * (max_len - len(chars[j]))

    word = ''
    for x in range(max_len):
        for y in range(5):
            word += chars[y][x]

    ret = word.replace('.', '')

    return ret


T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, column_word()))