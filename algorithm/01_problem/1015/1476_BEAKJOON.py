date = list(map(int, input().split()))
now = [1, 1, 1]
cnt = 1
while now != date:
    for i in range(3):
        now[i] += 1
    if now[0] > 15: now[0] = 1
    if now[1] > 28: now[1] = 1
    if now[2] > 19: now[2] = 1
    cnt += 1
print(cnt)
