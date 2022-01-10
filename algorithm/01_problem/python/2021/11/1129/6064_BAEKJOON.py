import sys
input = sys.stdin.readline

for tc in range(int(input())):
    M, N, x, y = map(int, input().split())
    if x > M or y > N:
        print(-1)
        continue

    f = e = 1
    e_list = [0] * 40001
    cnt = 1
    while True:
        if f == x and e == y:
            break

        elif f < x:
            cnt += 1
            f += 1
            e += 1
            if e > N:
                e = 1

        elif f == x:
            cnt += M
            e += M
            while e > N:
                e -= N

            if e_list[e]:
                cnt = -1
                break
            e_list[e] = 1

    print(cnt)
