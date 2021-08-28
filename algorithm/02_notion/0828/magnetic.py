import sys
sys.stdin = open('magnetic.txt', 'r')

T = 10
for tc in range(T):
    N = int(input())
    MAP = [['0'] * 100]
    MAP = MAP + [input().split() for _ in range(N)]
    MAP = MAP + [['0'] * 100]
    now = '1'
    cnt = 0
    for x in range(100):
        ret = False
        for y in range(1, 101):
            if MAP[y][x] == '1':
                ret = True
            if ret and MAP[y][x] != now and MAP[y][x] != '0':
                now = MAP[y][x]
                if now == '2':
                    cnt += 1
    print('#{} {}'.format(tc+1, cnt))

