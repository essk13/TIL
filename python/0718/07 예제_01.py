# 07 내장함수_01
# 다음의 결과와 같이 이름과 나이를 입력 받아
# 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

# input = 
# 홍길동
# 20
# output = 홍길동(은)는 2101년에 100세가 될 것입니다.

import datetime

def name_age():
    name = input('이름을 입력하십시오: ')
    age = int(input('나이를 입력하십시오: '))
    return name, age

def year_100(nage):
    plus_age = 100 - nage[1]
    year_100 = datetime.datetime.now().year + plus_age
    # datetime.datetime.now().  // year = 연도, month = 월, day = 일, hour = 시, minute = 분, second = 초, microsecond = 마이크로초
    print('{}(은)는 {}년에 100세가 될 것입니다.'.format(nage[0], year_100))

ret_nage = name_age()
ret_year = year_100(ret_nage)