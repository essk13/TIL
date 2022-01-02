import sys
sys.stdin = open('input.txt', 'r')


from copy import deepcopy

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
change_d = {1: 2, 2: 1, 3: 4, 4: 3}

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    MAP = [[0] * N for _ in range(N)]
    micro = []
    for i in range(K):
        r, c, mi, d = map(int, input().split())
        micro.append([r, c, d])
        MAP[r][c] = mi

    m = 0
    while m < M:
        new_Map = [[0] * N for _ in range(N)]
        ck_Map = [[0] * N for _ in range(N)]
        for j in range(K):
            r, c, d = micro[j]

            if d:
                nr, nc = r + dr[d], c + dc[d]
                if nr in (0, N - 1) or nc in (0, N - 1):
                    mi = MAP[r][c] // 2
                    if mi:
                        micro[j] = [nr, nc, change_d[d]]
                    else:
                        micro[j] = [nr, nc, 0]
                else:
                    mi = MAP[r][c]
                    micro[j] = [nr, nc, d]

                if ck_Map[nr][nc]:
                    if ck_Map[nr][nc][0] < mi:
                        micro[ck_Map[nr][nc][1]][2] = 0
                        ck_Map[nr][nc] = [mi, j]
                    else:
                        micro[j][2] = 0
                else:
                    ck_Map[nr][nc] = [mi, j]
                new_Map[nr][nc] += mi

        MAP = deepcopy(new_Map)
        m += 1

    ans = 0
    for i in range(N):
        ans += sum(MAP[i])
    print('#{} {}'.format(tc+1, ans))
