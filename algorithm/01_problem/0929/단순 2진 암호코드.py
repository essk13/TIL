import sys
sys.stdin = open('pw.txt', 'r')

p = ['0001101', '0011001', '0010011', '0111101', '0100011',
      '0110001', '0101111', '0111011', '0110111', '0001011']
num = list(range(10))
enc = dict(zip(p, num))

for tc in range(int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    sy = 0
    ex = 0
    for y in range(N):
        if code[y].count('1'):
            sy = y
            break

    for x in range(M-1, -1, -1):
        if code[sy][x] == '1':
            ex = x
            break

    pw = code[sy][ex-55:ex+1]
    dnc = ''
    for i in range(0, 56, 7):
        ret = enc[pw[i:i+7]]
        dnc += str(ret)

    check = 0
    for j in range(7):
        if j % 2:
            check += int(dnc[j])
        else:
            check += (3 * int(dnc[j]))

    print('#{}'.format(tc+1), end=' ')
    ans = check + int(dnc[7])
    if ans % 10:
        print(0)
    else:
        print(sum(map(int, list(dnc))))
