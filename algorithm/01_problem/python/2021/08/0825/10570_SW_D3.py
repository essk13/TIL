T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    cnt = 0

    for i in range(A, B+1):
        if (i ** 0.5) == int(i ** 0.5): # 정수 A가 정수 n의 제곱수인지 판별 후 맞다면 작업 수행
            a = str(i)
            b = str(int(i ** 0.5))
            ret = True
            for j in range(len(a)//2):  # A가 회문수인지 확인
                if a[j] != a[(len(a))-j-1]:
                    ret = False
                    break   # 회문수가 아니라면 아래 조건은 확인할 필요 없음
            if ret:
                for j in range(len(b)//2):  # A가 회문수라면 루트 A도 회문수인지 확인 
                    if b[j] != b[(len(b))-j-1]:
                        break
                else:
                    cnt += 1    # 둘 다 회문수이면 카운트

    print('#{} {}'.format(tc+1, cnt))
