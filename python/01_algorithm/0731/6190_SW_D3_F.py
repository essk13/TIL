def danzo(num):
    '''
    해당 숫자가 단조증가하는지 검사하는 함수
    '''
    num_str = str(num)
    # 인덱스를 이용하여 앞의 숫자가 뒷 숫자보다 크다면 False 아니면 True 반환
    for i in range(1, len(num_str)):
        if int(num_str[i-1]) > int(num_str[i]):
            return False
    return True

def monotone_increasing():
    '''
    숫자 리스트에서 두개의 숫자를 곱하여 단조 함수를 이용해
    단조증가하는 수 중 가장 큰 숫자를 반환하는 함수
    '''
    N = int(input())
    numbers = list(map(int, input().split()))

    max_dan = -1

    for i in range(N):
        for j in range(N):
            # 숫자 리스트에서 인덱스 i 값과 i보다 큰 인덱스 j를 곱하여 단조함수를 통해 확인
            if i < j:
                if numbers[i] * numbers[j] > max_dan and danzo(numbers[i] * numbers[j]) == True:
                    max_dan = numbers[i] * numbers[j]

    return max_dan

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {monotone_increasing()}')