# 05 흐름과 제어_반복문 예제_01
# 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

# input = 
# output = 
# 1번 학생은 88점으로 합격입니다.
# 2번 학생은 30점으로 불합격입니다.
# 3번 학생은 61점으로 합격입니다.
# 4번 학생은 55점으로 불합격입니다.
# 5번 학생은 95점으로 합격입니다.

Students_score = [
    {'번호' : 1, '점수' : 88},
    {'번호' : 2, '점수' : 30},
    {'번호' : 3, '점수' : 61},
    {'번호' : 4, '점수' : 55},
    {'번호' : 5, '점수' : 95}
]

for num in range(5):
    if Students_score[num]['점수'] >= 60:
        print("{}번 학생은 {}점으로 합격입니다.".format(Students_score[num]['번호'], Students_score[num]['점수']))
    else :
        print("{}번 학생은 {}점으로 불합격입니다.".format(Students_score[num]['번호'], Students_score[num]['점수']))