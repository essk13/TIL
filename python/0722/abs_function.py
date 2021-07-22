# 절대값 반환 함수
def abs_function(x):
    # 인자가 정수형인 경우
    if type(x) is int:
        if x > 0 :
            return x
        else :
            return -x
    # 인자가 부동소숫점 숫자형인 경우
    elif type(x) is float:
        if x > 0: 
            return x
        else :
            return -x
    # 인자가 복소수인 경우
    elif type(x) == complex:
        # a + bj = (a**2 + b**2) ** 0.5
        # .real = 정수부 .imag = 허수부
        x = (x.real**2 + x.imag**2) ** 0.5
        return x
    else :
        return 'Error'

print(abs_function(2+2j))
print(abs_function(-0.2))
print(abs_function(-8))