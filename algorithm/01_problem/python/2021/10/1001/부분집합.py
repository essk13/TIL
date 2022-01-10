def f(lv):
    global cnt
    if lv == len(arr):
        print(p, sum(p))
        cnt += 1
        return
    p.append(arr[lv])
    f(lv+1)
    p.pop()
    f(lv+1)


arr = [1, 3, 5, 9, 11]
p = []
cnt = 0
f(0)
print('cnt =', cnt)
