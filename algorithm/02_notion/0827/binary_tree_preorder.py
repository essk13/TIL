def preorder(t):
    if t:
        print(t, end=' ')
        if visited[t] == 0:
            visited[t] = 1
            preorder(left[t])
            preorder(right[t])


T = int(input())
for tc in range(T):
    V = int(input())
    E = V - 1
    visited = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    root = 1

    for i in range(E):
        st, ed = map(int, input().split())
        if left[st]:
            right[st] = ed
        else:
            left[st] = ed

    print('#{}'.format(tc+1), end=' ')
    preorder(root)
    print()
