def n_castle(level):
    cnt = 0
    # 끝까지 다 놓은 경우 카운트
    if level == N:
        cnt += 1
        return cnt
    for x in range(N):
        # 세로줄에 겹치는 경우가 존재하면 존재 불가능
        if used[x] == 1:
            continue
        # 룩을 둔 자리를 표시
        used[x] = 1
        cnt += n_castle(level + 1)
        # 룩을 뺀 다음 해당 자리 초기화
        used[x] = 0

    return cnt

T = 10
for tc in range(T):
    N = int(input())
    MAP = [[0] * N for _ in range(N)]
    # 룩을 둔 세로줄 체크
    used = [0] * N
    ans = n_castle(0)

    print('#{} {}'.format(tc+1, ans))