import sys
sys.stdin = open('smart.txt', 'r')


for tc in range(int(input())):
    N, O, M = map(int, input().split())
    p_num = input().split()
    p_operator = list(map(int, input().split()))
    W = int(input())

    used = [21] * 1000
    qu = []
    input_num = []
    for x in p_num:
        used[int(x)] = 1
        qu.append([x, 1, 0])
        input_num.append(x)

    for x in p_num:
        if x != '0':
            for y in p_num:
                used[int(x + y)] = 2
                qu.append([x + y, 2, 0])
                input_num.append(x + y)

    for x in p_num:
        if x != '0':
            for y in p_num:
                for z in p_num:
                    used[int(x + y + z)] = 3
                    qu.append([x + y + z, 3, 0])
                    input_num.append(x + y + z)

    ans = -1
    ret = 21
    while qu:
        now, cnt, o = qu.pop(0)
        now = int(now)
        if cnt > M:
            continue

        if now == W:
            if o:
                ret = min(cnt + 1, ret)
            else:
                ret = min(cnt, ret)
            continue

        for i in input_num:
            for j in p_operator:
                if j == 1:
                    na = now + int(i)
                elif j == 2:
                    na = now - int(i)
                elif j == 3:
                    na = now * int(i)
                elif j == 4 and int(i):
                    na = now // int(i)

                if 0 <= na <= 999 and cnt+len(i)+1 < used[na]:
                    used[na] = cnt + len(i) + 1
                    qu.append([na, cnt + len(i) + 1, o + 1])

    if ret < 21:
        ans = ret
    print(f'#{tc+1} {ans}')
