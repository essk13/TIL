import sys
sys.stdin = open('12585.txt', 'r')

def compare(N, M):
    for i in range(M - N + 1):
        for j in range(N):
            if str1[j] != str2[i+j]:
                break
        else:
            return 1

    return 0


T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    ans = compare(len(str1), len(str2))

    print('#{} {}'.format(tc+1, ans))