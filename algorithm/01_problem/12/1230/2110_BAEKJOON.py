import sys
input = sys.stdin.readline


def check(mid):
    '''
    중앙값을 기준으로 해당 거리만큼 떨어진
    공유기를 설치할 수 있는지 여부 판단
    '''
    idx = total = 0
    ck = C - 1
    while ck and idx < (N - 1):
        total += dist[idx]
        if total >= mid:
            ck -= 1
            total = 0
        idx += 1

    if ck:
        return False
    return True


N, C = map(int, input().split())

houses = [0] * N
for h in range(N):
    houses[h] = int(input())
houses.sort()

# 각 집간의 거리 리스트 계산
dist = [0] * (N - 1)
for h in range(1, N):
    dist[h-1] = houses[h] - houses[h-1]

# 시작 집과 가장 먼 집 간의 거리를 기준으로 중앙 값 계산
st, ed = 0, max(houses)
mid = (st + ed) // 2

ans = 0
while True:
    '''
    1) 해당 중앙값을 기준으로 설치할 수 없는 경우
        >> 중앙값을 끝 값으로 설정하여 새로운 중앙값 계산
    2) 해당 중앙값을 기준으로 설치할 수 있는 경우
        >> 중앙값을 시작 값으로 설정하여 새로운 중앙값 계산
    3) 끝값과 중앙값의 차이가 1인 경우 확인 종료
    '''
    res = check(mid)
    if res:
        ans = mid
        if mid + 1 == ed:
            break
        st = mid
        mid = (st + ed) // 2
    else:
        ed = mid
        mid = (st + ed) // 2

print(ans)
