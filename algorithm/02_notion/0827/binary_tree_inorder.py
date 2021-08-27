import sys
sys.stdin = open('input.txt', 'r')


def inorder(t):
    if t:
        if visited[t] == 0:
            visited[t] = 1
            inorder(left[t])
            print(node[t], end='')
            inorder(right[t])


def node_input():
    for i in range(V):
        ed1 = 0
        ed2 = 0
        node_in = input().split()
        if len(node_in) == 4:
            st = int(node_in[0])
            node_name = node_in[1]
            ed1 = int(node_in[2])
            ed2 = int(node_in[3])
        elif len(node_in) == 3:
            st = int(node_in[0])
            node_name = node_in[1]
            ed1 = int(node_in[2])
        else:
            st = int(node_in[0])
            node_name = node_in[1]

        if ed1:
            left[st] = ed1
        if ed2:
            if left[st]:
                right[st] = ed2
            else:
                left[st] = ed2

        node[st] = node_name


T = 10
for tc in range(T):
    V = int(input())
    visited = [0] * (V + 1)
    node = [''] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    root = 1
    node_input()

    print('#{}'.format(tc+1), end=' ')
    inorder(root)
    print()
