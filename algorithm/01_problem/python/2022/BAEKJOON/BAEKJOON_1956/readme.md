## [BAEKJOON 1956 운동](https://www.acmicpc.net/problem/1956) ![g4.png](C:\Users\sksms\Desktop\SSAFY\TIL\algorithm\01_problem\python\2022\BAEKJOON\BAEKJOON_13913\readme.assets\g4.png) (Python)

#### 입출력 / 제한

![입출력.PNG](readme.assets\입출력.PNG)

#### 풀이

가능한 모든 길을 이동하면서 조건에 따라 가지치기를 통해 문제를 해결하였다.

1. 1번 마을부터 V번 마을 순서로 가능한 길을 따라 출발
   
   a. 조건
   
       i. 현재 저장된 싸이클보다 크거나 같은 경우 확인 X
   
       ii. 현재 싸이클에서 사용한 길은 재사용 X

2. 출발한 마을에 다시 도착하면 저장된 싸이클 길이와 비교하여 더 작은 값 저장

#### 최종 코드

```python
import sys
from collections import deque
input = sys.stdin.readline


def bfs(st):
    global ans
    q = deque()
    used = [[0] * (V+1) for _ in range(V+1)]
    for nxt in range(1, V+1):
        if adj[st][nxt]:
            used[st][nxt] = 1
            q.append((nxt, adj[st][nxt]))

    while q:
        now, total = q.popleft()
        if now == st:
            ans = min(ans, total)

        if total >= ans:
            continue

        for nxt in range(1, V+1):
            if adj[now][nxt]:
                if used[now][nxt]:
                    continue
                used[now][nxt] = 1

                nt = total + adj[now][nxt]
                if nt >= ans:
                    continue
                q.append((nxt, total + adj[now][nxt]))
    return


V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c

ans = 4000001
for i in range(1, V+1):
    bfs(i)

if ans == 4000001:
    print(-1)
else:
    print(ans)

```

#### 느낀점

프로젝트를 진행하면서 알고리즘을 오랜만에 풀었는데 너무 어렵게 생각하고 있었던 것 같다. 이러면 무조건 시간초과가 날꺼라고 생각했는데 제출해보니 매우 여유롭게 통과했다. 그래도 보다 효율적인 방법이 있을지 찾아보고 다시 풀이해보도록 해야겠다.
