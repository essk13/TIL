import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def melting():
    ans = 0
    water = deque()
    swan = []
    for r in range(R):
        for c in range(C):
            '''
            1) 얼음이 아닌 경우 water 리스트에 저장
            1-1) 해당 위치의 녹는 날짜 0으로 초기화
            2) 백조 위치 저장
            '''
            if lake[r][c] != 'X':
                melt_lake[r][c] = 0
                water.append((r, c))
            if lake[r][c] == 'L':
                swan = [r, c]

    last = 0
    while water:
        '''
        주변 얼음의 녹는 날짜 지정(현재 위치 +1)
        '''
        r, c = water.popleft()
        last = melt_lake[r][c]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if melt_lake[nr][nc] != -1: continue

            melt_lake[nr][nc] = melt_lake[r][c] + 1
            water.append((nr, nc))
    # 백조 위치를 기준으로 며칠에 연결되는지 확인
    ans = isConnected(swan[0], swan[1], last)
    return ans


def isConnected(y, x, last_day):
    '''
    이분 탐색 활용
    1) 최소값 = 0, 최대값 = 녹는 날 중 최대값 
    '''
    st_day, ed_day = 0, last_day
    mid_day = (st_day + ed_day) // 2
    while True:
        # 최소, 최대값이 같은 경우 해당 날짜 반환
        if st_day == ed_day:
            return ed_day

        que = deque([(y, x)])
        visited = [[0] * C for _ in range(R)]
        visited[y][x] = 1
        while que:
            '''
            1) 중간값에 연결 가능한지 확인
            2) 연결 가능한 경우
                >> 최대값 = 중간값, 중간값 재계산
            3) 연결 불가능한 경우
                >> 최소값 = 중간값 +1, 중간값 재계산
            '''
            r, c = que.popleft()
            if (r, c) != (y, x) and lake[r][c] == 'L':
                ed_day = mid_day
                mid_day = (st_day + ed_day) // 2
                break

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                if visited[nr][nc]: continue
                if melt_lake[nr][nc] > mid_day: continue

                visited[nr][nc] = 1
                que.append((nr, nc))

        else:
            st_day = mid_day + 1
            mid_day = (st_day + ed_day) // 2


R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]
# 얼음이 녹는 날짜를 저장할 배열 생성
melt_lake = [[-1] * C for _ in range(R)]
ans = melting()
print(ans)
