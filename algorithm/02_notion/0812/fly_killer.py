def kill_sum(lst, j, i, m):
    kill = 0
    for y in range(j, j + m):
        for x in range(i, i + m):
            kill += lst[y][x]
    return kill

def f_killer():
    N, M = map(int, input().split())
    f_zone = [list(map(int, input().split())) for _ in range(N)]

    max_k = 0
    for j in range(N-M+1):
        for i in range(N-M+1):
            ret = kill_sum(f_zone, j, i, M)
            if ret > max_k:
                max_k = ret
            # kill = 0
            # for y in range(j, j+M):
            #     for x in range(i, i+M):
            #         kill += f_zone[y][x]
            #         if kill > max_k:
            #             max_k = kill

    return max_k

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, f_killer()))