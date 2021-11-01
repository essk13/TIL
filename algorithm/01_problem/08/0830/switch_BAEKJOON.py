def boy(n):
    for i in range(1, N+1):
        if i % n == 0:
            switch[i] += 1
            if switch[i] > 1:
                switch[i] = 0
    return


def girl(n):
    left = n
    right = n
    while 1 <= left and right < N+1 and switch[left] == switch[right]:
        left -= 1
        right += 1

    left += 1
    for i in range(left, right):
        switch[i] += 1
        if switch[i] > 1:
            switch[i] = 0


N = int(input())
switch = [0] + list(map(int, input().split()))
M = int(input())
for s in range(M):
    g, num = map(int, input().split())
    if g == 1:
        boy(num)
    else:
        girl(num)

for j in range(1, N+1):
    if j % 20 == 0:
        print(switch[j])
    else:
        print(switch[j], end=' ')
