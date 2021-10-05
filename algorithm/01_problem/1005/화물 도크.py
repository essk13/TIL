for tc in range(int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x:x[1])
    cnt = 1
    ed = lst[0][1]
    for i in range(1, N):
        if lst[i][0] >= ed:
            ed = lst[i][1]
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))
