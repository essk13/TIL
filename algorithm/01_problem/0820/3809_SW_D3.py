'''
화섭이의 정수 나열
'''

T = int(input())
for tc in range(T):
    N = int(input())
    num = ''

    # 입력받은 숫자의 길이가 N과 같아질 때까지 입력
    while len(num) < N:
        num += input().replace(' ', '')


    min_max = 0
    ans = 0
    check = 0
    z = 1
    for y in range(N):
        D = []
        for x in range(N - (z-1)):
            
            # 1자리 숫자, 2자리 숫자 ... 로 증가하면서 해당 값 누적
            if int(num[x:x+z]) not in D and int(num[x:x+z]) > (z - 1) * 9:
                D.append(int(num[x:x+z]))

        z += 1 # 자리 수 증가
        D.sort() # 비열한 쏘트
        for n in range(len(D)):
            if D[n] > min_max:
                # 최소값과 리스트의 최소값의 차가 1보다 크면 만들 수 없는 정수 존재
                if D[n] - min_max > 1:
                    # 최소값이 0이면 ans = 0
                    if min_max == 0:
                        ans = 0
                    # 아니면 ans = 최소값 + 1
                    else:
                        ans = min_max + 1
                    check = 1
                    break
                min_max = D[n]

        if check:
            break

    print('#{} {}'.format(tc+1, ans))