import sys
input = sys.stdin.readline


def check(mid):
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

dist = [0] * (N - 1)
for h in range(1, N):
    dist[h-1] = houses[h] - houses[h-1]

st, ed = 0, max(houses)
mid = (st + ed) // 2

ans = 0
while True:
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