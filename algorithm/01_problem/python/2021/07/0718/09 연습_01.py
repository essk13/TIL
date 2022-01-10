class Person:
    def __init__(self, name, age):  # self → 객체공간의 참조 전달
        self.name = name
        self.age = age
        print('{} 객체가 생성되었습니다.'.format(self.name))
    
    def __del__(self):              # self → 객체공간의 참조 전달
        print('{} 객체가 제거되었습니다.'.format(self.name))
        
    def to_str(self):               # 인스턴스 메서드 → self = name 필드와 age 필드를 문자열로 반환
        return '{}\t{}'.format(self.name, self.age)
    
    def get_name(self):             # __name 필드의 값을 반환하는 getter 메서드
        return self.__name
    
    def get_age(self):              # __age 필드의 값을 반환하는 getter 메서드
        return self.__age
    
    def set_age(self):              # __age 필드의 값을 변경하는 setter 메서드
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
            self.__age = age
            
members = [
    Person('홍길동', 20),
    Person('이순신', 45),
    Person('강감찬', 35)
]

members[0].set_age(-20)

for member in members:
    print(member.to_str())          # member 객체의 to_str 메서드를 호출하여 반환된 문자열 값 출력