import sys
sys.stdin = open('02.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    station = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        A = station[i]
        for j in range(N):
            if i == 0 and j == N - 1: continue
            if i == j or i + 1 == j or i - 1 == j: continue
            B = station[j]
            for x in range(N):
                if i == 0 and x == N - 1: continue
                if j == 0 and x == N - 1: continue
                if i == x or j == x: continue
                if i + 1 == x or i - 1 == x or j + 1 == x or j - 1 == x: continue
                C = station[x]
                for y in range(N):
                    if i == 0 and y == N - 1: continue
                    if j == 0 and y == N - 1: continue
                    if x == 0 and y == N - 1: continue
                    if i == y or j == y or x == y: continue
                    if i + 1 == y or i - 1 == y or j + 1 == y or j - 1 == y: continue
                    if x + 1 == y or x - 1 == y: continue
                    if i < x < j < y or i < y < j < x: continue
                    if j < x < i < y or j < y < i < x: continue
                    if x < i < y < j or x < j < y < i: continue
                    if y < i < x < j or y < j < x < i: continue
                    D = station[y]
                    ans = max(ans, (A+B) ** 2 + (C + D) ** 2)
    print('#{} {}'.format(tc+1, ans))
