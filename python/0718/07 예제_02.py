# 07 내장함수_02
# "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

# input = 
# output = 184

data = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# ord('A') = 65, ord('B') = 66, ord('C') = 67, ord('D') = 68
# 69 - ord(x) = 4, 3, 2, 1
score = sum(map(lambda x : 69 - ord(x), data))
print(score)