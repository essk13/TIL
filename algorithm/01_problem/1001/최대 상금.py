import sys
sys.stdin = open('input.txt', 'r')

def f(lv):
    global max_v
    v = ''
    for i in range(len(N)):
        v += N[i]
    if lv == C:
        if int(v) > max_v:
            max_v = int(v)
        return
    cnt = 0
    while cnt == 0:
        for i in range(len(N)):
            for j in range(i, len(N)):
                if j != i and N[i] < N[j] and N[j] != N[i]:
                    cnt += 1
                    N[i], N[j] = N[j], N[i]
                    f(lv+1)
                    N[i], N[j] = N[j], N[i]
        if cnt == 0 and C != 10:
            for i in range(len(N)):
                for j in range(i, len(N)):
                    if j != i and N[j] != N[i]:
                        cnt += 1
                        N[i], N[j] = N[j], N[i]
                        f(lv + 1)
                        N[i], N[j] = N[j], N[i]
        cnt += 1


for tc in range(int(input())):
    N, C = input().split()
    N = list(N)
    C = int(C)

    max_v = 0
    f(0)
    print('#{} {}'.format(tc+1, max_v))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645