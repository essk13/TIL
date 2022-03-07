## [BAEKJOON 14502 연구소](https://www.acmicpc.net/problem/14502) ![g5](../../0303/BAEKJOON_14503/readme.assets/g5.png) (Python)

#### 입출력 / 제한

 ![입출력](readme.assets/입출력.PNG)



#### 풀이

최대 사이즈가 8*8인 연구소이기 때문에 모든 경우의 수를 확인하여도 시간 내에 정답을 확인할 수 있을 것으로 판단되어 3개의 벽을 설치하는 경우의 수를 모두 확인하여 정답을 도출하였다.



1. 바이러스의 위치 정보를 저장하고 공백의 수를 카운트한다.

2. 3개의 벽을 설치하는 경우의 수를 3중 for문으로 모두 확인한다.

   ⓐ 0~M까지의 숫자를 반복하면서 M으로 나눈 몫과 나머지로 좌표값을 설정하여 확인하였다.

   ```python
   for x in range(N * M):
       xr, xc = x // M, x % M
   ```

3. BFS로 바이러스를 전파시킨 후 남은 감염되지 않은 공간의 수 중 최대값을 출력한다.



#### 최종 코드

```python
import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check():
    visited = [[0] * M for _ in range(N)]
    q = deque(virus)
    res = cnt
    for i, j in q:
        visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for d in range(4):
            nr, nc = i + dr[d], j + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visited[nr][nc] or MAP[nr][nc]: continue

            visited[nr][nc] = 1
            q.append([nr, nc])
            res -= 1
            if res <= ans:
                return 0

    return res


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

virus = []
cnt = -3
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 2:
            virus.append([r, c])
        elif MAP[r][c] == 0:
            cnt += 1

ans = 0
for x in range(N * M):
    xr, xc = x // M, x % M
    if MAP[xr][xc]: continue
    MAP[xr][xc] = 1
    for y in range(x + 1, N * M):
        yr, yc = y // M, y % M
        if MAP[yr][yc]: continue
        MAP[yr][yc] = 1
        for z in range(y + 1, N * M):
            zr, zc = z // M, z % M
            if MAP[zr][zc]: continue
            MAP[zr][zc] = 1
            ans = max(ans, check())
            MAP[zr][zc] = 0
        MAP[yr][yc] = 0
    MAP[xr][xc] = 0

print(ans)
```



#### 느낀점

없음