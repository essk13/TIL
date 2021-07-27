# 03 연산자 예제_01
# 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 인치는 2.54 센티미터입니다.

# input = 3
# output = 3.00 inch =>  7.62 cm


inch = int(input('inch를 입력하십시오: '))
cm = inch * 2.54

print('{:0.2f} inch =>  {} cm'.format(inch, cm))