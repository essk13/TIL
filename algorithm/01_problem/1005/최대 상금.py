import sys
sys.stdin = open('input.txt', 'r')


def dfs(lv):
    global max_v
    if lv == N:
        max_v = max(int(''.join(lst)), max_v)
        return
    for y in range(len(lst)):
        for x in range(y+1, len(lst)):
            lst[y], lst[x] = lst[x], lst[y]
            ck = ''.join(lst) + '#' + str(lv)
            if ck in visited: continue
            visited.add(ck)
            dfs(lv+1)
            lst[y], lst[x] = lst[x], lst[y]


for tc in range(int(input())):
    lst, N = input().split()
    lst = list(lst)
    N = int(int(N))
    visited = set()
    max_v = 0
    dfs(0)
    print('#{} {}'.format(tc+1, max_v))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645