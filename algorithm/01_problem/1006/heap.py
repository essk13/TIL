def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c1 = 2 * p
    c2 = (2 * p) + 1
    while c1 <= last:
        if c2 <= last:
            if tree[c1] >= tree[c2] and tree[c1] > tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                p = c1

            elif tree[c1] < tree[c2] and tree[c2] > tree[p]:
                tree[c2], tree[p] = tree[p], tree[c2]
                p = c2
            c1 = p * 2
            c2 = (p * 2) + 1
        else:
            if tree[c1] > tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                break


tree = [0] * 101
last = 0
a = [7, 2, 3, 9, 5]
for x in a:
    enq(x)
print(tree)
