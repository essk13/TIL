class Person:
    count = 0
    
    def __init__(self, name, age):               # 객체가 생성될 떄 마다 호출되는 __init__메서드
        self.__name = name
        self.__age = age
        Person.count += 1                        # 실행시 마다 count 1 증가
        print('{} 객체가 생성되었습니다.'.format(self.__name))
        
    def __del__(self):
        print('{} 객체가 제거되었습니다.'.format(self.__name))
        
    def to_str(self):
        return '{}\t{}'.format(self.__name, self.__age)
    
    @property
    def name(self):                 # 변수처럼 사용 가능, __name 필드값을 반환하는 getter 메서드 역할 수행
        return self.__name
    
    @property
    def age(self):                  # 변수처럼 사용 가능, __age 필드값을 반환하는 getter 메서드 역할 수행
        return self.__age
    
    @age.setter
    def age(self, age):             # 변수처럼 사용 가능, __age 필드값을 반환하는 setter 메서드 역할 수행
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age
        
    @classmethod
    def get_info(cls):              # cls = 클래스 자신에 대한 참조, 클래스 참조 정보가 인자로 넘어올 매개변수
        return '현재의 Person 클래스의 인스턴스는 총 {} 개입니다.'.format(cls.count)
                                                                     # cls.count == Person.count += 1
members = [
    Person('홍길동', 20),
    Person('이순신', 45),
    Person('강감찬', 35)
]

print(Person.get_info())           # Person 클래스를 통해 호출