import heapq

N, K = map(int, input().split())
ck = [21e8] * 100001

min_ = [(0, N)]
ans = 21e8
cnt = 0
while min_:
    sec, now = heapq.heappop(min_)
    if sec > ans: break
    if now == K:
        if ans > sec:
            ans = sec
            cnt = 1
        elif ans == sec: cnt += 1

    if K > now:
        if now + 1 < 100001 and ck[now+1] >= sec + 1:
            ck[now+1] = sec + 1
            heapq.heappush(min_, (sec+1, now+1))
        if now * 2 < 100001 and ck[now*2] >= sec + 1:
            ck[now*2] = sec + 1
            heapq.heappush(min_, (sec+1, now*2))
    if 0 <= now - 1 and ck[now-1] >= sec + 1:
        ck[now-1] = sec + 1
        heapq.heappush(min_, (sec+1, now-1))

print(ans)
print(cnt)