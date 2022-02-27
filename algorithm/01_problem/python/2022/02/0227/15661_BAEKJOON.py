import sys
input = sys.stdin.readline


def check():
    global ans
    team1 = []
    team2 = []
    for n in range(N):
        if used[n]:
            team1.append(n)
        else:
            team2.append(n)
    t1 = t2 = 0
    for i in range(len(team1) - 1):
        for j in range(i + 1, len(team1)):
            t1 += (adj[team1[i]][team1[j]] + adj[team1[j]][team1[i]])

    for i in range(len(team2) - 1):
        for j in range(i + 1, len(team2)):
            t2 += (adj[team2[i]][team2[j]] + adj[team2[j]][team2[i]])

    ans = min(ans, abs(t1 - t2))
    return


def make_team(now):
    if now == N:
        if sum(used) not in (0, N):
            check()
        return

    used[now] = 1
    make_team(now + 1)
    if now != 0:
        used[now] = 0
        make_team(now + 1)
    return


N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

ans = 21e8
used = [0] * N
make_team(0)
print(ans)
