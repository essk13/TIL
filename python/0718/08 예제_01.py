# 08 예외처리_01

width = input('폭을 입력하세요: ')
height = input('높이를 입력하세요: ')
area = 0

# try 문 실행
try:
    area = int(width) * int(height)
# 예외 발생 시 except 문 실행
except:
    print('숫자가 아닌 값이 입력되었습니다.')
# 예외 미발생 시 else 문 실행
else:
    print(f'{width} X {height} = {area}')
# 상관없이 finally 문 실행
finally:
	print('프로그램을 종료합니다...')