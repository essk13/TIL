def run_(p):
    for i in range(8):
        if p[i] > 0 and p[i+1] > 0 and p[i+2] > 0:
            return True
    return False


def triple(p):
    for i in p:
        if i == 3:
            return True
    return False

for tc in range(int(input())):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    ret = 0
    for i in range(len(card)):
        if i % 2:
            p2[card[i]] += 1
            ck1 = run_(p2)
            ck2 = triple(p2)
            if ck1 or ck2:
                ret = 2
                break
        else:
            p1[card[i]] += 1
            ck1 = run_(p1)
            ck2 = triple(p1)
            if ck1 or ck2:
                ret = 1
                break

    print('#{} {}'.format(tc+1, ret))
