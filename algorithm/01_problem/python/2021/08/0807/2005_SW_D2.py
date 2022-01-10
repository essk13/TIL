test_case = int(input())

for case in range(test_case):
    number = int(input())

    pascal = [[1]]

    for n in range(1, number):

        # 이전 줄의 숫자 개수가 1이라면 [1, 1] 추가
        if len(pascal[n-1]) == 1:
            pascal.append([1, 1])
        
        # 모든 line의 시작 숫자는 1
        # 이전 줄의 앞에서 두자리씩 더한 숫자를 line에 추가 후 1을 line에 추가
        else:
            line = [1]
            for i in range(1, len(pascal[n-1])):
                num = pascal[n-1][i-1] + pascal[n-1][i]
                line.append(num)
            line.append(1)
            pascal.append(line)

    print(f'#{case+1}')
    for idx in range(len(pascal)):
        print(*pascal[idx], end='\n')
