import sys
input = sys.stdin.readline


def inf_zero(num):
    if num == 21e8:
        num = 0
    return str(num)


n = int(input())
m = int(input())
cost = [[21e8] * n for _ in range(n)]

for bus in range(m):
    st, ed, c = map(int, input().split())
    cost[st-1][ed-1] = min(cost[st-1][ed-1], c)

for stop in range(n):
    cost[stop][stop] = 0
    for start in range(n):
        for end in range(n):
            cost[start][end] = min(cost[start][end], cost[start][stop] + cost[stop][end])

for i in range(n):
    print(' '.join(map(inf_zero, cost[i])))
