def winner(a, b):
    # 비기면 번호가 낮은 사람(a) 승
    # a가 이기면 a 반환 / b가 이기면 b 반환
    if card[a] == card[b] or \
        (card[a] == 1 and card[b] == 3) or \
        (card[a] == 2 and card[b] == 1) or \
        (card[a] == 3 and card[b] == 2):
        return a
    else :
        return b


def dfs(st, ed):
    if st == ed :
        return st
    # 각 그룹은 플레이어가 1명이 될 때까지 2개의 그룹으로 분열
    mid = (st + ed) // 2
    a = dfs(st, mid)
    b = dfs(mid+1, ed)
    # 플레이어가 1명이 되어 반환되면 반환된 2인 중 승자 반환
    ret = winner(a, b)
    return ret


T = int(input())
for tc in range(T):
    N = int(input())
    card = [-1]
    card += list(map(int, input().split()))
    ans = dfs(1, N)
    print('#{} {}'.format(tc+1, ans))