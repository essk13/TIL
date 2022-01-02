def triple(t):
    cnt = 1
    rt = 0
    for i in range(len(t)-1, -1, -1):
        rt += int(T[i]) * cnt
        cnt *= 3
    return rt


def checking():
    for i in range(len(B)):
        ob = B[i]
        for b in bi:
            if B[i] != b:
                B[i] = b
                break
        rb = int(''.join(B), 2)
        B[i] = ob
        for j in range(len(T)):
            ot = T[j]
            for t in ti:
                if T[j] != t:
                    T[j] = t
                    rt = triple(T)
                    if rb == rt:
                        return rb
                T[j] = ot

bi = ['0', '1']
ti = ['0', '1', '2']

for tc in range(int(input())):
    B = list(input())
    T = list(input())
    ans = checking()
    print('#{} {}'.format(tc+1, ans))
