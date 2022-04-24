import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move():
    q = deque([(0, 0, 1, K)])
    while q:
        i, j, c, k = q.popleft()
        if (i, j) == (N-1, M-1):
            return c
        for d in range(4):
            nr, nc = i + dr[d], j + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not visited[k][nr][nc]:
                if MAP[nr][nc] == '0':
                    visited[k][nr][nc] = 1
                    q.append((nr, nc, c + 1, k))

            if not visited[k-1][nr][nc]:
                if MAP[nr][nc] == '1' and k > 0:
                    visited[k-1][nr][nc] = 1
                    q.append((nr, nc, c + 1, k - 1))
    return -1


N, M, K = map(int, input().split())
MAP = [input().strip() for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(K+1)]
visited[0][0][0] = 1

print(move())
