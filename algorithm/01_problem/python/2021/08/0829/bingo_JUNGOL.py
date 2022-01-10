def bingo(number):
    for y in range(5):
        for x in range(5):
            if MAP[y][x] == number:
                BINGO[y] -= 1
                BINGO[x+5] -= 1
                if y == x:
                    BINGO[10] -= 1
                if y + x == 4:
                    BINGO[-1] -= 1
                return BINGO.count(0)


MAP = [list(map(int, input().split())) for _ in range(5)]
BINGO = [5] * 12
ret = 0
ans = 0
cnt = 0
for i in range(5):
    num = list(map(int, input().split()))
    if ret < 3:
        for j in range(5):
            cnt += 1
            ret = bingo(num[j])
            if ret >= 3:
                ans = cnt
                break

print(ans)
