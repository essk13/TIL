'''
최장거리 구하기
'''

def dfs(n):
    visited[n] = 1

    # 노드마다 거리 = 1
    length = 1
    max_ret = 0
    for i in range(N):
        if arr[n][i] == 1 and visited[i] == 0:
            ret = dfs(i)

            # 최종 이동 거리 + 현재 위치가 최장거리보다 길면 최고값 변경
            if 1 + ret > max_ret:
                max_ret = ret + 1
                length = 1 + ret
                
    # 이동했던 위치 초기화
    visited[n] = 0
    return length

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    
    # 간선의 방향이 없음으로 양 방향 모두 이동 가능하도록 배열 형성
    for i in range(M):
        x, y = map(int, input().split())
        arr[x-1][y-1] = 1
        arr[y-1][x-1] = 1

    visited = [0] * N
    max_len = 0
    
    # 각 노드마다 최장 이동거리 계산
    for j in range(N):
        ans = dfs(j)
        if ans > max_len:
            max_len = ans

    print('#{} {}'.format(tc+1, max_len))