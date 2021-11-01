from collections import deque
'''
FAIL
'''


def bfs(y, x, level, visit):
    queue = deque()
    queue.append([y, x, level, visit])
    ans = 0
    while queue:
        ny, nx, n_lv, visited = queue.popleft()
        ans = max(ans, n_lv)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < R and 0 <= tx < C:
                if board[ty][tx] not in visited:
                    queue.append([ty, tx, n_lv + 1, visited + board[ty][tx]])
    return ans


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]
print(bfs(0, 0, 1, board[0][0]))
