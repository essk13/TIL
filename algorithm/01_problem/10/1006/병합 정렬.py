def merge(l, r):
    ret = [0] * (len(l) + len(r))
    idx = 0
    li = ri = 0
    while li < len(l) and ri < len(r):
        if l[li] <= r[ri]:
            ret[idx] = l[li]
            li += 1
            idx += 1
        elif l[li] > r[ri]:
            ret[idx] = r[ri]
            ri += 1
            idx += 1

    while li < len(l):
        ret[idx] = l[li]
        li += 1
        idx += 1

    while ri < len(r):
        ret[idx] = r[ri]
        ri += 1
        idx += 1

    return ret


def merge_sort(st, ed):
    global cnt
    if st == ed: return [arr[st]]

    mid = (st + ed - 1) // 2
    l = merge_sort(st, mid)
    r = merge_sort(mid + 1, ed)
    ret = merge(l, r)

    if l[-1] > r[-1]:
        cnt += 1
    return ret


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(0, N-1)
    print('#{} {} {}'.format(tc+1, res[N//2], cnt))
