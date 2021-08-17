room = [0]*401
x = 0
for i in range(1, 400, 2):
    room[i] = x
    room[i+1] = x
    x += 1

T = int(input())
for tc in range(T):
    N = int(input())
    corridor = [0] * 201
    for i in range(N):
        r1, r2 = map(int, input().split())
        if r1 < r2:
            for j in range(room[r1], room[r2]+1):
                corridor[j] += 1
        else:
            for j in range(room[r2], room[r1]+1):
                corridor[j] += 1

    print('#{} {}'.format(tc+1, max(corridor)))