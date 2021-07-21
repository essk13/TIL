# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

# [예제]
# N이 3일 경우,
# 1 2 3
# 8 9 4
# 7 6 5
# N이 4일 경우,
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

# [제약사항]
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

snail = int(input())
snail_size = snail ** 2
snail_num = list(range(1, snail_size + 1))
snail_line = []

for number in range(1, snail_size + 1):
    if number <= snail:
        num = [number]
        snail_line += num
    
print(*snail_line)
snail_line = []

for number in range(1, snail_size + 1):
    if (snail * 2 - 1) <= number <= (snail * 3 - 2):
        num = [number]
        snail_line += num

last_line = snail_line.reverse()
print(last_line)
snail_line = []
