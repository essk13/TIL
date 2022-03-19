import sys
from collections import deque
input = sys.stdin.readline

for tc in range(int(input())):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append([a, s])

    time = [21e8] * (n + 1)
    time[c] = 0

    # 해킹에 걸린 시간 저장
    hack = deque([c])
    while hack:
        now = hack.popleft()
        for pc, sec in adj[now]:
            # 지금까지 걸린 시간이 기록된 시간보다 빠르면 변경
            if time[pc] > sec + time[now]:
                time[pc] = sec + time[now]
                hack.append(pc)

    ans1 = 0
    ans2 = 0
    for t in time:
        if t != 21e8:
            ans1 += 1
            # 모든 PC들 중 가장 늦게 해킹당한 PC의 시간이 최종 해킹 완료 시간
            ans2 = max(ans2, t)

    print(ans1, ans2)
