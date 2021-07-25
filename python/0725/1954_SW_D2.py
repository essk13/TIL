# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

# [제약사항]
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def snail():
    size = int(input())
    size_2 = size
    num_list = list(range(1, size**2+1))
    snail_size = []

    for n in range(size):
        snail_size.append([])
        for i in range(size):
            snail_size[n].append(0)

    for a in range(1, size+1):
        if num_list == []:
            break

        for y in range(size-size_2, size-size_2+1):
            for x in range(a-1, size_2):
                snail_size[y][x] = num_list.pop(0)
                if num_list == []:
                    break

        for x in range(size_2-1, size_2):
            for y in range(a, size_2):
                snail_size[y][x] = num_list.pop(0)
                if num_list == []:
                    break

        for y in range(size_2-1, size_2):
            for x in range(size_2-2, size-size_2-1, -1):
                snail_size[y][x] = num_list.pop(0)
                if num_list == []:
                    break

        for x in range(size-size_2, size-size_2+1):
            for y in range(size_2-2, size-size_2, -1):
                snail_size[y][x] = num_list.pop(0)
                if num_list == []:
                    break

        size_2 -= 1

    for line in range(size):
        print(*snail_size[line], end='\n')

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    result = snail()