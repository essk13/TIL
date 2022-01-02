import sys
sys.stdin = open('input.txt', 'r')

def max_p(e, mp):
    global max_percent
    # 0퍼센트인 경우 생략
    if mp == 0:
        return
    # 현재 최고 확륙보다 작은 경우 생략
    if max_percent > mp:
        return
    # 모든 업무를 배정한 뒤 성공활률 점검
    if e == N:
        max_percent = mp
        return
    # 작업 할당
    for n in range(N):
        if done[n] == 0:
            done[n] = 1
            percent = (P[e][n] / 100) * mp
            max_p(e + 1, percent)
            done[n] = 0
    return


for tc in range(int(input())):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    done = [0] * N
    max_percent = 0
    max_p(0, 1)
    ans = max_percent * 100
    print('#{} {:.6f}'.format(tc + 1, ans))
