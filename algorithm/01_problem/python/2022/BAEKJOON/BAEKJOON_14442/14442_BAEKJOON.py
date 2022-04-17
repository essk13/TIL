import sys, heapq
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move():
    q = [(1, -K, 0, 0)]
    while q:
        i, j, c, k = heapq.heappop(q)
        if (i, j) == (N-1, M-1):
            return c
        for d in range(4):
            nr, nc = i + dr[d], j + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc]:
                continue

            if MAP[nr][nc] == '1' and k < 0:
                visited[nr][nc] = c + 1
                heapq.heappush(q, (c + 1, k + 1, nr, nc))
            elif MAP[nr][nc] == '0':
                visited[nr][nc] = c + 1
                heapq.heappush(q, (c + 1, k, nr, nc))
    return -1


N, M, K = map(int, input().split())
MAP = [input().strip() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

print(move())
