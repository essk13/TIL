import sys, time
sys.stdin = open('input.txt', 'r')


def get_company_pos():
    global N, M

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 'A':
                return i, j


def get_room_pos():
    global N, M, L

    ret = [()] * (L + 1)
    for i in range(N):
        for j in range(M):
            if Map[i][j].isdigit() and Map[i][j] != '0':
                ret[int(Map[i][j])] = (i, j)
    return ret


def get_shortest_time_walk():
    # 모든 집의 위치는 다르며, 회사 위치인 'A'와 월세방 집의 위치가 같은 경우는 없다.
    global N, M, L, ax, ay

    ret = [float('inf')] * (L + 1)
    for i in range(1, L + 1):
        rx, ry = room_pos[i]
        ret[i] = (abs(ax - rx) + abs(ay - ry)) * 30
    return ret


def get_shortest_time_subway():
    global L, ax, ay
    from heapq import heappush, heappop

    graph = {i:[] for i in range(1, L + 1)}
    for route in stations:
        fee = route[-1]
        for k in range(len(route) - 2):
            a, b = route[k], route[k + 1]
            graph[a].append((fee, b))
            graph[b].append((fee, a))

    dist = [[float('inf')] * (L + 1) for _ in range(L + 1)]
    for i in range(1, L + 1):
        dist[i][i] = 0
        heap = [(0, i)]
        while heap:
            fee, cur = heappop(heap)

            if fee < dist[i][cur]:
                continue

            for f, nxt in graph[cur]:
                if dist[i][cur] + f < dist[i][nxt]:
                    dist[i][nxt] = dist[i][cur] + f
                    heappush(heap, (dist[i][cur] + f, nxt))

    ret = [float('inf')] * (L + 1)
    for i in range(1, L + 1):
        for k in range(1, L + 1):
            sx, sy = room_pos[k]
            walking_time = (abs(ax - sx) + abs(ay - sy)) * 30
            ret[i] = min(ret[i], dist[i][k] + walking_time)
    return ret


def get_infra_score(plus=1, minus=1, scope=2):
    global L
    from collections import deque

    ret = [0] * (L + 1)
    for i in range(1, L + 1):
        q = deque([room_pos[i]])
        visit = [[0] * M for _ in range(N)]
        visit[room_pos[i][0]][room_pos[i][1]] = 1
        while q:
            x, y = q.popleft()
            if visit[x][y] > scope:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
                    if Map[nx][ny].isalpha():
                        if 'B' <= Map[nx][ny] <= 'M':
                            ret[i] += plus
                        elif 'N' <= Map[nx][ny] <= 'Y':
                            ret[i] -= minus
    return ret


if __name__ == '__main__':
    start = time.time()
    M, N, n, m = map(int, input().split())
    Map = [list(input().split()) for _ in range(N)]
    L = int(input())  # 월세방 개수
    monthly_fee = [0] + list(map(int, input().split()))
    stations = []
    for _ in range(int(input())):
        stations.append(list(map(int, input().split())) + [int(input())])

    ax, ay = get_company_pos()
    t1 = time.perf_counter()
    print('get_company_pos', round(t1 - start, 2))
    room_pos = get_room_pos()
    t2 = time.perf_counter()
    print('get_room_pos', round(t2 - t1, 2))
    shortest_time_walk = get_shortest_time_walk()
    t3 = time.perf_counter()
    print('get_shortest_time_walk', round(t3 - t2, 2))

    shortest_time_subway = get_shortest_time_subway()
    t4 = time.perf_counter()
    print('get_shortest_time_subway', round(t4 - t3, 2))
    infra_score = get_infra_score()
    t5 = time.perf_counter()
    print('get_infra_score', round(t5 - t4, 2))
    room_scores = [100] * (L + 1)
    for i in range(1, L + 1):
        t = min(shortest_time_walk[i], shortest_time_subway[i])
        room_scores[i] -= t // m + monthly_fee[i] // n
        room_scores[i] += infra_score[i]

    room_scores[0] = 0
    M = max(room_scores)
    for idx, score in enumerate(room_scores):
        if score == M:
            print(idx)
    finish = time.perf_counter()
    print('최종', round(finish - start, 2))

    end = time.time()
    print(f'{end - start:.5f} sec')
