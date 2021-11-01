# def sort_sum(a1, a2):
#     ret = []
#     idx1 = 0
#     idx2 = 0
#     while idx1 < len(a1) and idx2 < len(a2):
#         if a1[idx1] <= a2[idx2]:
#             ret.append(a1[idx1])
#             idx1 += 1
#         elif a1[idx1] > a2[idx2]:
#             ret.append(a2[idx2])
#             idx2 += 1
#     while idx1 < len(a1):
#         ret.append(a1[idx1])
#         idx1 += 1
#     while idx2 < len(a2):
#         ret.append(a2[idx2])
#         idx2 += 1
#     print(ret)
#     return
#
# a1 = [1, 3, 3, 7, 8]
# a2 = [2, 3, 4, 6]
# sort_sum(a1, a2)


def merge(l, r):
    ret = []
    li = ri = 0
    while li < len(l) and ri < len(r):
        if l[li] <= r[ri]:
            ret.append(l[li])
            li += 1
        elif l[li] > r[ri]:
            ret.append(r[ri])
            ri += 1

    while li < len(l):
        ret.append(l[li])
        li += 1

    while ri < len(r):
        ret.append(r[ri])
        ri += 1
    return ret


def merge_sort(st, ed):
    global stage
    if st == ed:
        return [arr[st]]

    mid = (st + ed) // 2
    l = merge_sort(st, mid)
    r = merge_sort(mid + 1, ed)
    ret = merge(l, r)

    print('{}단계 : {} + {} = {}'.format(stage, l, r, ' '.join(map(str, ret))))
    stage += 1
    return ret


# arr = [5, 7, 3, 2, 9, 1, 4, 6, 8, 0]
arr = [4, 7, 2, 1, 8, 5]
stage = 1
print('원 본 : {}'.format(' '.join(map(str, arr))))
res = merge_sort(0, len(arr) - 1)
print('결 과 : {}'.format(' '.join(map(str, res))))
