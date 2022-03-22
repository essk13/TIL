from collections import defaultdict

for tc in range(int(input())):
    n = int(input())
    pre_rank = list(map(int, input().split()))
    rank = [defaultdict(lambda: 0) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i > j:
                rank[pre_rank[i]][pre_rank[j]] = 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if rank[a][b]:
            del(rank[a][b])
        else:
            rank[a][b] = 1

        if rank[b][a]:
            del(rank[b][a])
        else:
            rank[b][a] = 1

    ans = [0] * n
    for team in range(1, n + 1):
        if ans[len(rank[team])]:
            print("IMPOSSIBLE")
            break
        ans[len(rank[team])] = team
    else:
        print(' '.join(map(str, ans)))
