import sys
input = sys.stdin.readline

# 코드 베이스 (달팽이)
# def get_number():
#     r = c = N // 2
#     d = 0
#     cnt1 = cnt2 = 0
#     cnt3 = 1
#     n = 1
#     while n < N ** 2:
#         r, c = r + dr[d], c + dc[d]
#         number[r][c] = n
#         cnt1 += 1
#         n += 1
#
#         if cnt1 == cnt3:
#             d += 1
#             cnt1 = 0
#             cnt2 += 1
#             if cnt2 == 2:
#                 cnt1 = cnt2 = 0
#                 cnt3 += 1
#
#         if d > 3:
#             d = 0


def shoot(d, l):
    sr = sc = N // 2
    for i in range(l):
        sr, sc = sr + dr[blizzard[d]], sc + dc[blizzard[d]]
        if sr < 0 or sr >= N or sc < 0 or sc >= N: continue
        MAP[sr][sc] = 0
    return


def change_to_line():
    r = c = N // 2
    d = 0
    cnt1 = cnt2 = 0
    cnt3 = 1
    n = 1
    while n < N ** 2:
        r, c = r + dr[d], c + dc[d]
        line[n] = MAP[r][c]
        cnt1 += 1
        n += 1

        if cnt1 == cnt3:
            d += 1
            cnt1 = 0
            cnt2 += 1
            if cnt2 == 2:
                cnt1 = cnt2 = 0
                cnt3 += 1

        if d > 3:
            d = 0
    return


def change_to_curve():
    r = c = N // 2
    d = 0
    cnt1 = cnt2 = 0
    cnt3 = 1
    n = 1
    while n < N ** 2:
        r, c = r + dr[d], c + dc[d]
        MAP[r][c] = line[n]
        cnt1 += 1
        n += 1

        if cnt1 == cnt3:
            d += 1
            cnt1 = 0
            cnt2 += 1
            if cnt2 == 2:
                cnt1 = cnt2 = 0
                cnt3 += 1

        if d > 3:
            d = 0
    return


def move():
    new_line = [n for n in line if n != 0]
    new_line = [0] + new_line + [0] * (N ** 2 - (len(new_line) + 1))
    return new_line


def explosion():
    global nums
    num = st = re = 0
    for n in range(1, N ** 2):
        if num != line[n]:
            if n - st > 3:
                line[st:n] = [0] * (n - st)
                nums[num] += ((n - st) * num)
                re += 1
            num = line[n]
            st = n
    return re


def grouping():
    n = 1
    new_line = [0] * (N ** 2)
    num = cnt = 0
    for i in range(1, N ** 2):
        if num != line[i]:
            if num:
                new_line[n] = cnt
                n += 1
                if n >= N ** 2:
                    break
                new_line[n] = num
                n += 1
                if n >= N ** 2:
                    break
            num = line[i]
            cnt = 1
        elif num == line[i]:
            cnt += 1

    return new_line


dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
blizzard = {1: 3, 2: 1, 3: 0, 4: 2}

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
number = [[0] * N for _ in range(N)]

nums = [0] * 4

for m in range(M):
    d, l = map(int, input().split())
    # 파편 발사
    shoot(d, l)

    # 펼치기
    line = [0] * (N ** 2)
    change_to_line()

    # 구슬 이동
    line = move()

    # 구슬 폭파
    re = 1
    while re:
        re = explosion()
        line = move()

    # 구슬 그룹화
    line = grouping()

    # 말기
    change_to_curve()

print(sum(nums))
