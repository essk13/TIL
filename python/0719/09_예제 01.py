# 09 객체지향_01
# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

# input = 89, 90, 100

# outpu = 국어, 영어, 수학의 총점: 279

class Score:

    def __init__(self, scores):
        self.__kor = scores[0]
        self.__math = scores[1]
        self.__eng = scores[2]
    
    @property
    def kor(self):
        return self.__kor

    @property
    def math(self):
        return self.__math
    
    @property
    def eng(self):
        return self.__eng

    def total_score(self):
        total = self.__kor  + self.__math + self.__eng
        print('국어, 영어, 수학의 총점: {}'.format(total))

score = input('점수를 입력하십시오(국어, 수학, 영어): ')
score = list(map(int, score.split(', ')))

ret_total = Score(score)
result = ret_total.total_score()