def circular():
    N, M = map(int, input().split())
    chars = [list(input()) for _ in range(N)]

    for y in range(N):
        for i in range(N-M+1):
            lst_x = []
            lst_y = []
            for x in range(i, i + M):
                lst_x.append(chars[y][x])
                lst_y.append(chars[x][y])
            if lst_x == lst_x[::-1]:
                return ''.join(lst_x)
            elif lst_y == lst_y[::-1]:
                return ''.join(lst_y)

    # for x in range(N):
    #     for i in range(N-M+1):
    #         lst = []
    #         for y in range(i, i + M):
    #             lst.append(chars[y][x])
    #         if lst == lst[::-1]:
    #             return ''.join(lst)

T = int(input())

for tc in range(T):
    print('#{} {}'.format(tc+1, circular()))