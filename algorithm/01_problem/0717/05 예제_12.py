# 05 흐름과 제어_반복문 예제_12
# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

# input = 9
# output = 1001

number = int(input('숫자를 입력하십시오: '))
# print('{:b}'.format(number))
num_2 = []
i = number

while i >= 2:
    cnt = i % 2
    num_2.append(cnt)
    if i == 2:
        num_2.append(1)
    i = i // 2

# 리스트 역순 변환 시 .reverse 는 루프 사용 불가 ('reverse 메소드 반환값 != 리스트'기 때문)
# 그래서 [::-1]을 사용하는 것을 추천
print(''.join(list(map(str, num_2[::-1]))))