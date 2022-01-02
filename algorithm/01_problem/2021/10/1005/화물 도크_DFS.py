import sys
sys.stdin = open('bf.txt', 'r')


def work(lv, ed, mc):
    global cnt
    if lv == N:
        cnt = max(cnt, mc)
        return
    c = 1
    for i in range(1, N+1):
        if lst[i][0] >= ed and done[i] == 0:
            c = 0
            done[i] = 1
            work(lv+1, lst[i][1], mc+1)
            done[i] = 0
    if c:
        cnt = max(cnt, mc)
        return


for tc in range(int(input())):
    N = int(input())
    lst = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
    done = [0] * (N + 1)
    done[0] = 1
    cnt = 0
    work(0, 0, 0)
    print('#{} {}'.format(tc+1, cnt))
