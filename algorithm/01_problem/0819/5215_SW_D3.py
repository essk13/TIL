def cook(n, kcal, score):
    global max_score
    visited[n] = 1
    kcal += ingredient[n][1]
    score += ingredient[n][0]
    if kcal > L:
        visited[n] = 0
        return
    if kcal <= L and score > max_score:
        max_score = score
    for i in range(N):
        if i != n and visited[i] == 0:
            cook(i, kcal, score)
    visited[n] = 0
    return


T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    visited = [0] * N
    for i in range(N):
        cook(i, 0, 0)

    print('#{} {}'.format(tc+1, max_score))