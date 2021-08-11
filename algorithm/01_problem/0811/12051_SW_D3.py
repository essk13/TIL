def freecell():
    N, PD, PG = list(map(int, input().split()))

    win_t = PG * N / 100
    lose_t = (100 - PG) * N / 100

    for game in range(1, N+1):
        for win_d in range(1, game+1):
            if win_d > win_t or game - win_d > lose_t:
                break

            elif win_d / game * 100 == PD:
                return 'Possible'

    return 'Broken'

TC = int(input())

for case in range(TC):
    print('#{} {}'.format(case+1, freecell()))