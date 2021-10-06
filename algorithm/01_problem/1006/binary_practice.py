def b_search(st, ed, arr):
    global ans
    mid = (st + ed) // 2

    if st > ed: return -1

    if arr[mid] == target:
        ans = mid
        n_st = mid + 1
        b_search(n_st, ed, arr)

    else:
        n_ed = mid - 1
        b_search(st, n_ed, arr)


arr = [
    '#########_____',
    '###____________',
    '##########__'
]
target = '#'
ans = -1
for i in arr:
    b_search(0, len(i) - 1, i)
    print(ans)