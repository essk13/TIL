num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
gns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
ntog = dict(zip(num, gns))
gton = dict(zip(gns, num))

T = int(input())
for case in range(T):
    tc, N = input().split()
    gnums = input().split()
    cnt = [0]*10

    for i in range(int(N)):
        cnt[gton[gnums[i]]] += 1

    print(tc)
    for j in range(10):
        for c in range(cnt[j]):
            print(ntog[j], end=' ')