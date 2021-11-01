def partition(st, ed):
    p = arr[st]
    s, e = st + 1, ed
    while s <= e:
        while s <= e and arr[s] <= p:
            s += 1
        while s <= e and arr[e] >= p:
            e -= 1
        if s < e:
            arr[s], arr[e] = arr[e], arr[s]
    arr[st], arr[e] = arr[e], arr[st]
    return e


def q_sort(st, ed):
    if st < ed:
        p = partition(st, ed)
        q_sort(st, p - 1)
        q_sort(p + 1, ed)


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    q_sort(0, N - 1)
    print('#{} {}'.format(tc+1, arr[N//2]))
