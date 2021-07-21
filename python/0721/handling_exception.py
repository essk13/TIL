try:
    num = int(input('숫자를 입력하세요: '))
    print(100 / num)
except ValueError:
    print('※ 숫자가 아닙니다 ※')
except ZeroDivisionError:
    print('※ 0으로 나눌 수 없습니다 ※')
except:
    print('※ Error 발생 ※')