import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def escape(position):
    que = deque([position])
    # 음수는 지나지 않은 길
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    # 시작점 0으로 초기화
    visited[position[0]][position[1]] += 1
    while que:
        r, c = que.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위를 벗어나거나 방문한 지점, 벽은 무시
            if nr < 0 or nr >= h + 2 or nc < 0 or nc >= w + 2: continue
            if visited[nr][nc] >= 0: continue
            if MAP[nr][nc] == '*': continue

            # 문을 통과하는 경우 카운트 +1
            if MAP[nr][nc] == '#':
                visited[nr][nc] = visited[r][c] + 1
                que.appendleft((nr, nc))
            # 통로를 지나는 경우 이전 카운트 유지
            else:
                visited[nr][nc] = visited[r][c]
                que.append((nr, nc))
    return visited


for tc in range(int(input())):
    h, w = map(int, input().split())
    # 벽 옆으로 빈 공간 생성
    MAP = [['.' for _ in range(w + 2)]] + [['.'] + list(input().strip()) + ['.'] for _ in range(h)] + [['.' for _ in range(w + 2)]]
    prisoner = []
    for r in range(h + 2):
        for c in range(w + 2):
            if MAP[r][c] == '$':
                prisoner.append((r, c))
            if len(prisoner) == 2:
                break

    # 탈옥수와 상근이의 이동루트 별 개방한 문의 개수 기록
    prisoner1 = escape(prisoner[0])
    prisoner2 = escape(prisoner[1])
    sang_geun = escape((0, 0))

    ans = 100 ** 2
    for r in range(h + 2):
        for c in range(w + 2):
            '''
            1) 3명이 모두 만나는 지점 확인
            2) 각각의 개방한 문 누적
            3) 해당 지점이 문인 경우 중복된 2개의 문 제거
            4) 이전 값과 현재 값 비교
            '''
            if prisoner1[r][c] >= 0 and prisoner2[r][c] >= 0 and sang_geun[r][c] >= 0:
                res = prisoner1[r][c] + prisoner2[r][c] + sang_geun[r][c]
                if MAP[r][c] == '#':
                    res -= 2
                ans = min(ans, res)
    print(ans)
