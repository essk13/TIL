def b_search(st, ed, lst):
    arr = lst
    ret = -1
    mid = (st + ed) // 2
    if st > ed: return -1

    if arr[0][mid] == target and arr[0][mid+1] == '_': return mid

    if arr[0][mid] != target:
        n_ed = mid - 1
        ret = b_search(st, n_ed, arr)
    elif arr[0][mid] == target:
        n_st = mid + 1
        ret = b_search(n_st, ed, arr)
    return ret


# arr = [1, 2, 5, 7, 15, 20, 300]
# st = 0
# ed = len(arr) - 1
# mid = (st + ed) // 2
# target = int(input())
#
# # ans = -1
# ans = b_search(st, ed)
# while st <= ed:
#     if arr[mid] == target:
#         ans = mid
#         break
#     if arr[mid] > target:
#         ed = mid - 1
#         mid = (st + ed) // 2
#     elif arr[mid] < target:
#         st = mid + 1
#         mid = (st + ed) // 2


arr = ['#########_____']
arr2 = ['###____________']
arr3 = ['##########__']

target = '#'
ans1 = b_search(0, len(arr[0]) - 1, arr)
ans2 = b_search(0, len(arr2[0]) - 1, arr2)
ans3 = b_search(0, len(arr3[0]) - 1, arr3)

print(ans1)
print(ans2)
print(ans3)