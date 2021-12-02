import sys, time
sys.stdin = open('input.txt', 'r')

from collections import deque
start = time.time()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def surrounding_infra(row, col):
    ret_plus = 0
    ret_minus = 0
    que = deque()
    used = [[0 for _ in range(C)] for _ in range(R)]
    used[row][col] = 1
    que.append([row, col, 0])
    while que:
        rr, cc, cnt = que.popleft()
        if cnt >= 2:
            continue
        for i in range(4):
            r_idx = rr + dr[i]
            c_idx = cc + dc[i]
            if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                continue
            if used[r_idx][c_idx] == 1:
                continue
            if 'B' <= MAP[r_idx][c_idx] <= 'M':
                ret_plus += 1
            if 'N' <= MAP[r_idx][c_idx] <= 'Y':
                ret_minus += 1
            used[r_idx][c_idx] = 1
            que.append([r_idx, c_idx, cnt+1])

    return (ret_plus, ret_minus)


# 걷는시간 칸당 30분
# 지하철은 정거장마다 받은 가중치
def shortest_distance_to_A(row, col):
    global room_cnt, graph, home_to_company_dict
    room_cand = int(MAP[row][col])
    que = deque()
    used = [0] * (room_cnt+1)
    for g in graph[room_cand]:
        used[g[1]] = 1
        que.append(g)
    while que:
        # 지하철로 갈수 있는 정거장이 다 뽑히고
        # 기존의 home_to_company_dict에 저장되있는 현재 걸어서 가는 거리보다 그게 빠르면
        # 갈아 끼워준다.
        val, pos = que.popleft()
        # 더 작으면 갱신
        if home_to_company_dict[pos] + val < shortest_dict[room_cand]:
            shortest_dict[room_cand] = home_to_company_dict[pos] + val
        # 이후 다른정거장 que에 append
        for station in graph[pos]:
            if used[station[1]]:
                continue
            used[station[1]] = 1
            que.append((station[0]+val, station[1]))
    return


# def my_solution(row, col):
#     # 가점
#     # 감점
#     global total
#     plus_score, minus_score = surrounding_infra(row, col)
#     print(f'{MAP[row][col]}의 집 정보')
#     print(f'주변 인프라 가점: {plus_score}')
#     print(f'주변 인프라 감점: {minus_score}')
#     # 출퇴근 거리 및 시간?
#     # 월급 가점 계산 및 total에 반영?
#
#     return


C, R, M, N = map(int, input().split())

MAP = [list(input().split()) for _ in range(R)]

room_cnt = int(input())
room_cost_lst = list(map(int, input().split()))

station_cnt = int(input())
station_lst = []
station_cost = []

# 최단 거리 dict
shortest_dict = {i:0 for i in range(1, room_cnt+1)}

total = {i:100 for i in range(1, room_cnt+1)}

for idx in range(station_cnt):
    temp = list(map(int, input().split()))
    station_lst.append(temp)
    station_cost.append(int(input()))

print(C, R, M, N)
print(MAP)
print(room_cnt)
print(room_cost_lst)
print(station_cnt)
print(station_lst)
print(station_cost)

company = [-1, -1]
home_to_company_dict = dict()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'A':
            company = [r, c]
            break

room_location = []

for r in range(R):
    for c in range(C):
        if MAP[r][c].isdigit():
            # my_solution(r, c)
            room_location.append([r, c])
            home_to_company = abs(r-company[0]) + abs(c-company[1])
            home_to_company_dict[int(MAP[r][c])] = home_to_company * 30
            shortest_dict[int(MAP[r][c])] = home_to_company * 30

print(home_to_company_dict)


graph = {i:[] for i in range(1, room_cnt+1)}

print(graph)
cnt = 0
for route in station_lst:
    fee = station_cost[cnt]
    for j in range(len(route) - 1):
        a, b = route[j], route[j+1]
        graph[a].append((fee, b))
        graph[b].append((fee, a))
    cnt += 1

print(graph)

for y, x in room_location:
    plus_score, minus_score = surrounding_infra(y, x)
    shortest_distance_to_A(y, x)
    total[int(MAP[y][x])] += plus_score
    total[int(MAP[y][x])] -= minus_score

for idx in range(1, room_cnt+1):
    total[idx] -= (shortest_dict[idx]//N)
    total[idx] -= (room_cost_lst[idx-1]//M)

print(graph)
print(f'각 집의 출근 시간 : {shortest_dict}')
print(f'total: {total}')
end = time.time()
print(f'{end - start:.5f} sec')