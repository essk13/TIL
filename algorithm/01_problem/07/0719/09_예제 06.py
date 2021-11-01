# 09 객체지향_06
# Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
# Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
# length * length 값을 반환하는 메서드로 오버라이딩합니다.

# input = 

# outpu = 정사각형의 면적: 9

class Shape:
    pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.__length = length
    
    @property
    def lenght(self):
        return self.__length
    
    def area(self):
        return self.__length ** 2

sq_length = int(input('정사각형의 한 변의 길이를 입력하십시오: '))
sq = Square(sq_length)

print(f'정사각형의 면적: {sq.area()}')