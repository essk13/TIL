def start_index():
    '''
    미로의 출발지점 좌표를 반환하는 함수
    {st_y: start_y_index, st_x: start_x_index}
    # 출발지점의 값 == 2 #
    '''
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                st_y, st_x = y, x
    return st_y, st_x

def maze_run(now_y, now_x):
    '''
    출발점에서 도착점으로 이동가능한 경로의 존재여부를 반환하는 함수
    {now_y: now_y_index, now_x: now_x_index}
    # 출발지점 == 2, 도착지점 == 3,
    # 길 == 0, 벽 == 1
    '''
    cnt = 0
    visited[now_y][now_x] = 1   # 현재 좌표를 방문지점으로 등록
    if maze[now_y][now_x] == 3: # 현재 좌표의 값이 도착지점이면 1 반환
        return 1
    if cnt == 1:    # 도착지점으로 이동가능한 경로가 하나라도 존재하면 prunning
        return
    for i in range(4):  # 현재 좌표에서 델타 탐색 방향으로 이동 시 좌표가 미로 범위를 벗어나지 않으면서 방문지점이 아닌 경우 재귀 호출
        if 0<= now_y + dy[i] < N and 0 <= now_x + dx[i] < N and \
            maze[now_y+dy[i]][now_x+dx[i]] != 1 and \
            visited[now_y+dy[i]][now_x+dx[i]] == 0:
            cnt += maze_run(now_y + dy[i], now_x + dx[i])
    visited[now_y][now_x] = 0   # 방문지점 여부 초기화
    return cnt

# 탐색 방향을 변경하기 위한 델타 y, x
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N = int(input().rstrip())
    maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # prunning을 위한 방문여부 판독 배열
    st_y, st_x = start_index()  # 시작 y, x 좌표
    ans = maze_run(st_y, st_x)
    print('#{} {}'.format(tc+1, ans))