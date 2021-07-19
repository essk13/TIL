# 09 객체지향_02
# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
# 메서드를 호출하는 코드를 작성해봅시다.

# input = 

# outpu = 
# 대한민국
# 대한민국

class Korean:
    
    def __init__(self, nation):
        self.__nation = nation

    @property
    def nation(self):
        return self.__nation

    def printNationality(self):
        print(f'{self.nation}\n{self.nation}')

nation_kor = '대한민국'
nation_korea = Korean(nation_kor)
print_nation = nation_korea.printNationality()


