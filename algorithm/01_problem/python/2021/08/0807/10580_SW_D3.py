def utility_pole():
    line = int(input())

    A = []
    B = []
    for n in range(line):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)

    cross = 0
    for i in range(line):
        for j in range(i+1, line):
            if A[i] < A[j] and B[i] < B[j] or A[i] > A[j] and B[i] > B[j]:
                pass
            else:
                cross += 1

    return cross

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {utility_pole()}')