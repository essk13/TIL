# 09 객체지향_04
# 반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
# 생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.

# input = 

# outpu = 원의 면적: 12.56

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    def area(self):
        return self.__radius ** 2 * 3.14

radius_input = int(input('반지름을 입력하십시오: '))
area_circle = Circle(radius_input)

print(f'원의 면적: {area_circle.area()}')