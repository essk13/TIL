def mirror():
    word = input()
    origin = ['b', 'd', 'p', 'q']
    mirror = ['d', 'b', 'q', 'p']
    otom = dict(zip(origin, mirror))
    n_word = ''

    for i in range(len(word)):
        n_word += otom[word[i]]

    return n_word[::-1]

T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, mirror()))