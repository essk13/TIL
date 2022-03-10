import sys, heapq
from copy import deepcopy
sys.stdin = open('input.txt')

'''
94.5%
FAIL
'''

def move(now, nxt):
    if adj[now][nxt]:
        return adj[now][nxt]
    return 0


def r_move(now, nxt):
    if adj[nxt][now]:
        return adj[nxt][now]
    return 0


def bfs():
    heap = [(0, start, [0] * len(traps))]
    while heap:
        cnt, now, change = heapq.heappop(heap)
        if now == end:
            return cnt

        for i in range(1, n + 1):
            if linked[now][i]:
                if isTrap[now] >= 0 and isTrap[i] >= 0:
                    nn, ni = isTrap[now], isTrap[i]
                    if (change[nn], change[ni]) in [(1, 1), (0, 0)]:
                        res = move(now, i)
                    else:
                        res = r_move(now, i)

                elif isTrap[now] >= 0:
                    nn = isTrap[now]
                    if change[nn]:
                        res = r_move(now, i)
                    else:
                        res = move(now, i)

                elif isTrap[i] >= 0:
                    ni = isTrap[i]
                    if change[ni]:
                        res = r_move(now, i)
                    else:
                        res = move(now, i)

                else:
                    res = move(now, i)

                if res:
                    if isTrap[i] >= 0:
                        n_chg = deepcopy(change)
                        n_chg[isTrap[i]] = (n_chg[isTrap[i]] + 1) % 2
                        heapq.heappush(heap, (cnt + res, i, n_chg))
                    else:
                        heapq.heappush(heap, (cnt + res, i, deepcopy(change)))
    return


n, start, end = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(3)]
traps = list(map(int, input().split()))

adj = [[0] * (n + 1) for _ in range(n + 1)]
linked = [[0] * (n + 1) for _ in range(n + 1)]
for p, q, s in roads:
    linked[p][q] = 1
    linked[q][p] = 1
    if adj[p][q]:
        adj[p][q] = min(s, adj[p][q])
    else:
        adj[p][q] = s

isTrap = [-1] * (n + 1)
for t in range(len(traps)):
    isTrap[traps[t]] = t

ans = bfs()
print(ans)
