def min_sum(idx_y, total):
    '''
    N*N 2차원 배열에서 가로/세로 중복되지 않도록
    N개의 숫자를 선택한 합의 최소값을 구하는 함수
    {idx_y:index_y, total: minimum_sum}  
    '''
    global minimum
    if idx_y == N - 1 and total < minimum:  # y 인덱스가 N-1이면서 부분집합의 합이 최소값보다 작은 경우 최소값 변경
        minimum = total
        return
    if total >= minimum: # 부분집합의 합이 최소값 이상인 경우 prunning
        return
    for i in range(N):
        if used_x[i] == 0:  # x 인덱스가 겹치지 않는 경우에 재귀 호출
            used_x[i] = 1   # x 인덱스 사용 여부 저장
            min_sum(idx_y+1, total+arr[idx_y+1][i])
            used_x[i] = 0   # x 인덱스 사용 여부 초기화
    return

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used_x = [0] * N    # x 인덱스를 중복해서 사용하는 경우 방지 (겹치는 경우에는 prunning)
    minimum = 21e8      # 최소값을 구하기 위해 충분히 큰 정수 저장
    min_sum(-1, 0)      # 재귀 함수에서 y 인덱스 0을 포함하기 위해 -1에서 시작
    print('#{} {}'.format(tc+1, minimum))