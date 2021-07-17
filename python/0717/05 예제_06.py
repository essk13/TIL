# 05 흐름과 제어_반복문 예제_06
# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

# input = 
# output = {'A': 3, 'O': 3, 'B': 2, 'AB': 2}

blood_types = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood_type = ['A', 'O', 'B', 'AB']
people = []

for num in range(1, 2):
    people.append(blood_types.count('A'))
    people.append(blood_types.count('O'))
    people.append(blood_types.count('B'))
    people.append(blood_types.count('AB'))

print(dict(zip(blood_type, people)))