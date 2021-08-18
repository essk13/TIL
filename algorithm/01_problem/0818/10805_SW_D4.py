T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    change = [list(map(int, input().split())) for _ in range(Q)]
    ans = set()

    for i in range(Q+1):
        o = 1
        for j in range(Q):
            if i == j and o + 1 < N:
                o += 1
            A = change[j][0]
            B = change[j][1]
            if A == o:
                o = B
            elif B == o:
                o = A

        ans.add(o)

    for i in range(Q+1):
        o = 1
        for j in range(Q):
            if i == j and o - 1 > 0:
                o -= 1
            A = change[j][0]
            B = change[j][1]
            if A == o:
                o = B
            elif B == o:
                o = A

        ans.add(o)

    print('#{} {}'.format(tc+1, len(ans)))