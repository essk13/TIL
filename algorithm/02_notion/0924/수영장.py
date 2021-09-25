def check(day):
    c1 = plan[day] * D
    c2 = M
    return min(c1, c2)

def tree():

    return

T = int(input())
for tc in range(T):
    D, M, T, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    mc = [0] * 12

    for i in range(12):
        if plan[i] == 0:
            continue
        mc[i] = check(i)


    cost = min(Y, sum(mc))
    print('#{} {}'.format(tc+1, cost))