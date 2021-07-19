# 09 객체지향_05
# 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
# 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

# input = 

# outpu = 사각형의 면적: 20

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        print(f'사각형의 면적: {self.__width * self.__height}')

width_input = int(input('가로값을 입력하십시오: '))
height_input = int(input('세로값을 입력하십시오: '))
rectangle_input = Rectangle(width_input, height_input)
ret_Rec = rectangle_input.area()