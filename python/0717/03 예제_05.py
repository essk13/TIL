# 03 연산자 예제_05
# 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

# input = 
# output = 혼합된 소금물의 농도: 6.67%


salt = 0.2 * 100
water1 = 100 - salt
water2 = 200

salt_water = (salt / (salt + water1 + water2)) * 100

print('혼합된 소금물의 농도: {:.2f} %'.format(salt_water))