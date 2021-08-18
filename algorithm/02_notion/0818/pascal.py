T = int(input())
for tc in range(T):
    N = int(input())
    tri = []
    for i in range(1, N+1):
        tri.append([0]*i)

    print('#{}'.format(tc+1))
    for y in range(N):
        for x in range(len(tri[y])):
            tri[y][0] = 1
            tri[y][-1] = 1
            if y != 0 and 0 < x < len(tri[y]) - 1:
                tri[y][x] = tri[y-1][x-1] + tri[y-1][x]

        print(*tri[y])