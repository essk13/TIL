import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check(y, x):
    '''
    BFS 탐색을 통해 새로운 클러스터인지 판단
    조건: 현재 미네랄 덩어리와 바닥과의 연결 여부
    >> 새로운 클러스터인 경우 gravity 함수 호출
    '''
    que = deque([(y, x)])
    cluster = [(y, x)]
    outline = [(y, x)]
    stop = False
    while que:
        r, c = que.popleft()
        if r == R - 1:
            stop = True

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if visited[nr][nc]: continue
            if cave[nr][nc] == '.': continue

            visited[nr][nc] = 1
            que.append((nr, nc))
            cluster.append((nr, nc))

            # 현재 클러스터의 바닥 부분을 리스트에 저장
            nnr = nr + 1
            if nnr >= R: continue
            if cave[nnr][nc] == '.':
                outline.append((nr, nc))

    if stop: return False

    gravity(cluster, outline)
    return True


def gravity(cluster, outline):
    '''
    1. 동굴에서 클러스터 제거
    2. 클러스터의 바닥부분이 다른 미네랄 또는 바닥과 접촉할 때까지 한칸씩 아래로 하강
    3. 접촉(겹친)경우 해당 위치보다 1칸 위에 제거한 클러스터 생성
    '''
    for r, c in cluster:
        cave[r][c] = '.'

    stop = False
    res = 1
    while True:
        for r, c in outline:
            if r + res >= R or cave[r + res][c] == 'x':
                stop = True
                res -= 1
                break
        else:
            res += 1
        if stop: break

    for r, c in cluster:
        cave[r + res][c] = 'x'
    return


R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
H = list(map(int, input().split()))

for turn in range(1, N + 1):
    # 현재 턴이 홀수인 경우 좌측, 짝수인 경우 우측에서 막대기 던지기
    if turn % 2:
        d = 0
        di = 'left'
    else:
        d = C - 1
        di = 'right'

    h = R - H[turn - 1]
    while 1:
        # 미네랄을 만날 때까지 이동 후 해당 미네랄 파괴
        if cave[h][d] == 'x':
            cave[h][d] = '.'
            break

        # 끝까지 이동 후 미네랄이 없으면 종료
        if di == 'left':
            if d == C - 1:
                break
            d += 1
        else:
            if d == 0:
                break
            d -= 1

    visited = [[0] * C for _ in range(R)]
    for i in range(4):
        # 파괴된 미네랄의 상, 하, 좌, 우의 미네랄을 시작점으로 BFS 탐색
        nr, nc = h + dr[i], d + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
        if visited[nr][nc]: continue
        if cave[nr][nc] == '.': continue

        visited[nr][nc] = 1
        res = check(nr, nc)
        if res:
            break

for i in range(R):
    print(''.join(cave[i]))
