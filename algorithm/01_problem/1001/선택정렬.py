def s_sort(lv):
    if lv == len(arr) - 1: return
    # for i in range(lv+1, len(arr)):
    #     if arr[lv] > arr[i]:
    #         arr[lv], arr[i] = arr[i], arr[lv]
    n = min(arr[lv:])
    idx = arr[lv:].index(n)
    arr[lv], arr[idx+lv] = arr[idx+lv], arr[lv]
    s_sort(lv+1)


arr = list(map(int, input().split()))
s_sort(0)
print(arr)