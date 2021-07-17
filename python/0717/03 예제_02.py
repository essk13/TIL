# 03 연산자 예제_02
# 킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 킬로그램은 2.2046 파운드입니다.

# input = 90
# output = 90.00 kg =>  198.41 lb


kg = int(input('kg을 입력하십시오: '))
lb = kg * 2.2046

print('{:.2f} kg =>  {:.2f} lb'.format(kg, lb))