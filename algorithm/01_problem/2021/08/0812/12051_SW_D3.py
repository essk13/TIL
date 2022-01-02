def freecell():
    N, PD, PG = list(map(int, input().split()))
    result = True

    if N < 100:
        result = False
        for game in range(1, N+1):
            # for win in range(game+1):
            if PD * game / 100 == int(PD * game / 100):
                result = True

    if result == False:
        return 'Broken'

    if PD < 100 and PG == 100:
        return 'Broken'

    if PD > 0 and PG == 0:
        return 'Broken'

    return 'Possible'

TC = int(input())

for case in range(TC):
    print('#{} {}'.format(case+1, freecell()))