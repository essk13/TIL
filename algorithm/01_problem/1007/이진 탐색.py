def b_search(st, ed, p):
    global cnt
    mid = (st + ed) // 2
    if st > ed: return

    if A[mid] == tg:
        cnt += 1
        return

    if A[mid] > tg and p != 1:
        b_search(st, mid - 1, 1)

    if A[mid] < tg and p != 2:
        b_search(mid + 1, ed, 2)
    return


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        tg = B[i]
        b_search(0, N - 1, 0)
    print('#{} {}'.format(tc+1, cnt))
