def is_exist(y, x, y2, x2):
    for r in range(y, y2+1):
        for c in range(x, x2+1):
            if ground[r][c] == 0:
                return 0
    return 1

def get_sum(y, x, y2, x2):
    total = 0
    for r in range(y, y2+1):
        for c in range(x, x2+1):
            total += ground[r][c]
    return total


T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(H)]
    max_g = 0

    for y in range(H):
        for x in range(W):

            for y2 in range(y, H):
                for x2 in range(x, W):
                    ret = is_exist(y, x, y2, x2)
                    if ret:
                        ans = get_sum(y, x, y2, x2)
                        if ans > max_g:
                            max_g = ans

    print('#{} {}'.format(tc+1, max_g))