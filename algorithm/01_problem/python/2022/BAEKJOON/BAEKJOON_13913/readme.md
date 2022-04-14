## [BAEKJOON 13913 숨바꼭질 4](https://www.acmicpc.net/problem/13913) ![g4.png](C:\Users\sksms\Desktop\SSAFY\TIL\algorithm\01_problem\python\2022\BAEKJOON\BAEKJOON_13913\readme.assets\g4.png) (Python)

#### 입출력 / 제한

![입출력.PNG](C:\Users\sksms\Desktop\SSAFY\TIL\algorithm\01_problem\python\2022\BAEKJOON\BAEKJOON_13913\readme.assets\입출력.PNG)

#### 풀이

heap과 BFS를 사용하여 가장 낮은 시간을 소모하면서 동생의 위치에 도착하는 경우를 확인하는 방법으로 문제를 해결하였다.

1. 형 위치 X에서 +1, -1, x2 를 한 위치를 지금까지 소모한 시간 +1을 하여 방문
   
   a. 방문 시 시간이 더 적은 경우만 방문 허용
   
   b. 이동시마다 방문 지점을 경로에 추가

2. 동생의 위치에 도착하는 경우 계산 종료 및 정답 출력

#### 최종 코드

```python
import heapq


N, K = map(int, input().split())
sp = [0] * 100001
sp[N] = 1

q = [(0, N, str(N))]

while q:
    sec, n, path = heapq.heappop(q)
    if n == K:
        print('{}\n{}'.format(sec, path))
        break

    if n - 1 >= 0 and (sp[n-1] == 0 or sp[n-1] > sec + 1):
        sp[n-1] = sec + 1
        heapq.heappush(q, (sec + 1, n - 1, path + ' ' + str(n - 1)))

    if n + 1 <= 100000 and (sp[n+1] == 0 or sp[n+1] > sec + 1):
        sp[n+1] = sec + 1
        heapq.heappush(q, (sec + 1, n + 1, path + ' ' + str(n + 1)))

    if 2 * n <= 100000 and (sp[2*n] == 0 or sp[2*n] > sec + 1):
        sp[2*n] = sec + 1
        heapq.heappush(q, (sec + 1, 2 * n, path + ' ' + str(2 * n)))

```

#### 느낀점

DP를 사용하여 보다 빠르게 문제를 해결 가능할 것 같은데 역시 DP부분에서 부족한 점이 많은 것 같다. 이 부분은 꾸준히 문제를 풀이하면서 보완해야할 것 같다.
