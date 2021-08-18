### stack ###
# lst = [3, 7, 5, 9, 2, 8]
# st = []
#
# for i in range(len(lst)):
#     print(lst[i], end=' ')
#     st.append(lst[i])
#
# while st:
#     print(st.pop(-1), end=' ')

### 재귀함수 ###
# def abc(n):
#     if n == 3:
#         return
#     print(n, end= ' ')
#     abc(n + 1)
#     print(n, end=' ')
#     return
#
# abc(0)


def binary_search(lst, st, ed, mid, key):
    global ret
    if lst[mid] == key:
        ret = '찾았다'
        return
    elif lst[st] > key or lst[ed] < key:
        ret =  '못찾았다'
        return
    elif lst[mid] < key:
        st_r = mid
        mid_r = int((st_r + ed) / 2)
        binary_search(lst, st_r, ed, mid_r, key)
        return
    elif lst[mid] > key:
        ed_r = mid
        mid_r = int((st + ed_r) / 2)
        binary_search(lst, st, ed_r, mid_r, key)
        return
    else:
        ret = '못찾았다'
        return


arr = [1,2,5,7,9,15,17]

l = 0
r = len(arr) - 1
m = int((l + r) / 2)

ret = None
binary_search(arr, l, r, m, 3)

print(ret)