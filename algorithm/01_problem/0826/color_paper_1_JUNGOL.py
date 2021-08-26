N = int(input())
paper = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(N):
    y, x = map(int, input().split())
    st_y = y - 9
    st_x = x
    ed_y = y
    ed_x = x + 9

    for r in range(st_y, ed_y+1):
        for c in range(st_x, ed_x+1):
            if paper[r][c] == 0:
                paper[r][c] = 1
                cnt += 1

print(cnt)