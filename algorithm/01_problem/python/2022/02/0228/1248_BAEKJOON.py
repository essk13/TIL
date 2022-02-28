def check(idx):
    total = 0
    for n in range(idx, -1, -1):
        total += ans[n]
        r = partial[n][idx]
        if (total == 0 and r != 0) or (total > 0 and r <= 0) or (total < 0 and r >= 0):
            return False
    return True


def find(idx):
    if idx == N:
        return True

    r = partial[idx][idx]
    if r == 0:
        ans[idx] = 0
        return find(idx + 1)

    for n in range(1, 11):
        ans[idx] = partial[idx][idx] * n
        if check(idx) and find(idx+1):
            return True
    return


N = int(input())
arr = list(input())
partial = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        res = arr.pop(0)
        if res == '+':
            partial[i][j] = 1
        elif res == '-':
            partial[i][j] = -1

ans = [0] * N
find(0)
print(' '.join(map(str, ans)))
