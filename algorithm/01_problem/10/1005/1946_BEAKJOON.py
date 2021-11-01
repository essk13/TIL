import sys
input = sys.stdin.readline

for tc in range(int(input())):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    p.sort()
    ms = p[0][1]
    cnt = 1
    for i in range(1, N):
        if p[i][1] < ms:
            cnt += 1
            ms = p[i][1]
    print(cnt)