# 05 흐름과 제어_반복문 예제_07
# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

# input = 
# output = 454

scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
score = []
i = 0

while i <= 9:
    if scores[i] >= 80:
        score_80 = scores.pop(i)
        scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
        score.append(score_80)

    i += 1

print(sum(score))