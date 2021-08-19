def path_find(start, goal):
    visited[start] = 1
    ret = 0
    if start == goal:
        return 1

    for i in range(100):
        if arr[start][i] == 1 and visited[i] == 0:
            ret += path_find(i, goal)

    return ret


T = 10
for tc in range(T):
    case, P = map(int, input().split())
    arr = [[0]*100 for _ in range(100)]
    visited = [0] * 100
    path = list(map(int, input().split()))

    for i in range(0, len(path), 2):
        arr[path[i]][path[i+1]] = 1

    ans = path_find(0, 99)

    print('#{} {}'.format(case, ans))