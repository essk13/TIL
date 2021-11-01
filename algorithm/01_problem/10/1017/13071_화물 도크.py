for tc in range(int(input())):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    p.sort(key=lambda x:x[1])
    cnt = 0
    ed = 0
    for i in range(N):
        if p[i][0] >= ed:
            cnt += 1
            ed = p[i][1]
    print('#{} {}'.format(tc+1, cnt))