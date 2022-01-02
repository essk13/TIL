def pre(now):
    print(tree[now][0], end='')
    if tree[now].count('.') == 2: return
    for i in range(1, 3):
        if tree[now][i] != '.':
            for j in range(N):
                if tree[j][0] == tree[now][i]:
                    pre(j)
    return


def post(now):
    if tree[now].count('.') == 2:
        print(tree[now][0], end='')
        return
    for i in range(1, 3):
        if tree[now][i] != '.':
            for j in range(N):
                if tree[j][0] == tree[now][i]:
                    post(j)
    print(tree[now][0], end='')
    return


def inorder(now):
    if now == N + 1:
        return
    if tree[now].count('.') == 2:
        print(tree[now][0], end='')
        return
    for i in range(1, 3):
        if tree[now][i] == '.':
            inorder(N+1)
        elif tree[now][i] != '.':
            for j in range(N):
                if tree[j][0] == tree[now][i]:
                    inorder(j)
        if i == 1:
            print(tree[now][0], end='')
    return


N = int(input())
tree = [input().split() for _ in range(N)]

pre(0)
print()
inorder(0)
print()
post(0)