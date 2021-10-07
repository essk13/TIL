def charging(st, bty, chg):
    global cnt
    if st + bty >= station[0]:
        cnt = min(cnt, chg)
        return

    if bty < 0 or chg >= cnt: return

    if bty >= station[st]:
        charging(st + 1, bty - 1, chg)
    else:
        charging(st + 1, station[st] - 1, chg + 1)
        charging(st + 1, bty - 1, chg)
    return


for tc in range(int(input())):
    station = list(map(int, input().split()))
    cnt = 21e8
    charging(2, station[1] - 1, 0)
    print('#{} {}'.format(tc+1, cnt))
