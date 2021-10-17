def merge(left, right):
    l = len(left)
    r = len(right)
    li = ri = idx = 0
    ret = [0] * (l + r)
    while li < l and ri < r:
        if left[li] < right[ri]:
            ret[idx] = left[li]
            li += 1
        else:
            ret[idx] = right[ri]
            ri += 1
        idx += 1

    while li < l:
        ret[idx] = left[li]
        li += 1
        idx += 1
    while ri < r:
        ret[idx] = right[ri]
        ri += 1
        idx += 1
    return ret


def merge_sort(st, ed):
    if st == ed: return [arr[st]]
    mid = (st + ed) // 2
    left = merge_sort(st, mid)
    right = merge_sort(mid+1, ed)
    ret = merge(left, right)
    return ret


arr = list(map(int, input().split()))
N = len(arr)
ans = merge_sort(0, N-1)
print(*ans)
