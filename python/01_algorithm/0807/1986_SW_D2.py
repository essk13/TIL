def zigzag_number():
    number = int(input())

    numbers = []

    # 홀수는 그대로, 짝수는 음의 정수로 변환하여 리스트화
    for num in range(1, number+1):
        if num % 2:
            numbers.append(num)
        else:
            numbers.append(-num)

    # 리스트의 합을 반환
    return sum(numbers)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {zigzag_number()}')