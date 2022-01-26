import sys
from copy import deepcopy
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check(n, y, x):
    # n이 단어의 길이와 같은 경우(단어 완성) >> 경로 += 1
    if n == len(word):
        return 1
    # 현 위치 && n번 인덱스에서 완성 경로 존재 >> 경로 += 현 위치 경로 수
    if used[y][x][n] > -1:
        return used[y][x][n]

    # 탐색 위치의 경로 초기화
    used[y][x][n] = 0
    for i in range(4):
        nr, nc = y, x
        for _ in range(K):
            nr += dr[i]
            nc += dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if MAP[nr][nc] != word[n]: continue
            # 현 위치에 완성된 경로 수 누적
            used[y][x][n] += check(n + 1, nr, nc)

    return used[y][x][n]


N, M, K = map(int, input().split())
MAP = [input().strip() for _ in range(N)]
word = input().strip()

ans = 0
# 해당 경로를 지날 때 완성 가능한 경로 저장
used = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c in range(M):
        # 시작 알파벳인 경우 경로 탐색
        if MAP[r][c] == word[0]:
            ans += check(1, r, c)

print(ans)
