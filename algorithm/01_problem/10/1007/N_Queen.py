def queen(y):
    cnt = 0
    if y == N: return 1
    for x in range(N):
        can = True
        lv = 1
        while lv <= y and can and ck[x] == 0:
            for i in range(2):
                r, c = y - lv, x + dx[i] * lv
                if 0 <= r and 0 <= c < N:
                    if (r, c) in ck:
                        can = False
                        break
            lv += 1

        if ck[x] == 0 and can:
            ck[x] = (y, x)
            cnt += queen(y + 1)
            ck[x] = 0
    return cnt


dx = [1, -1]

for tc in range(int(input())):
    N = int(input())
    ck = [0] * N
    ans = queen(0)
    print('#{} {}'.format(tc+1, ans))
