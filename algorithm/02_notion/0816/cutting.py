def cutting():
    N = input()

    cnt = 0
    total = 0
    ret = []
    for i in range(len(N)):
        if N[i] == '(' and N[i+1] == ')':
            total += cnt
            continue
        if N[i] == '(':
            cnt += 1
            total += 1
        elif N[i] == ')' and N[i-1] != '(':
            cnt -= 1

    print(ret)

    return total

T = int(input())

for tc in range(T):
    print('#{} {}'.format(tc+1, cutting()))