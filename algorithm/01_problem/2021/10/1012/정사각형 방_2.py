import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('room.txt', 'r')


def move(r, c):
    if memo[r][c] > 0:  # memo 기록 존재 = return
        return memo[r][c]

    max_ret = 1
    for i in range(4):
        ny, nx = r + dy[i], c + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if room[ny][nx] == room[r][c] + 1:
                ret = move(ny, nx) + 1
                max_ret = max(ret, max_ret)

    memo[r][c] = max_ret
    return max_ret


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0] * N for _ in range(N)]

    max_cnt = 0
    min_st = 21e8
    for y in range(N):
        for x in range(N):
            cnt = move(y, x)
            if max_cnt < cnt:
                max_cnt = cnt
                min_st = room[y][x]
            elif max_cnt == cnt:
                min_st = min(min_st, room[y][x])

    print('#{} {} {}'.format(tc+1, min_st, max_cnt))


#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5
