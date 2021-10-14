def Find(a):
    if MST[a] == a:
        return a
    ret = Find(MST[a])
    MST[a] = ret
    return ret


def Union(a, b):
    global group
    na = Find(a)
    nb = Find(b)
    if na != nb:
        MST[na] = nb
        member[nb] += member[na]
        member[na] = 0
        group -= 1
    return


for tc in range(int(input())):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    MST = list(range(N+1))
    member = [1] * (N+1)
    group = N
    for i in range(0, len(paper), 2):
        na = Find(paper[i])
        nb = Find(paper[i+1])
        if na != nb:
            Union(na, nb)
    max_ = 0
    # print('#{} {}'.format(tc+1, group))
    print(max(member))
