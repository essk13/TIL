def dfs(day, total):
    global profit
    if total > profit:
        profit = total
    for i in range(day+1, N+1):
        if adj[day][i] == 1 and done[i] == 0:
            done[i] = 1
            dfs(i, total + price[i])
            done[i] = 0
    return


N = int(input())
adj = [[0] * (N+1) for _ in range(N+1)]
price = [0] * (N+1)
done = [0] * (N+1)

for i in range(1, N+1):
    T, P = map(int, input().split())
    if i + T - 1 > N:
        done[i] = 1
        continue
    for j in range(i+T, N+1):
        adj[i][j] = 1
    price[i] = P

profit = 0
for day in range(1, N+1):
    if done[day] == 0:
        done[day] = 1
        dfs(day, price[day])
        done[day] = 0

print(profit)
