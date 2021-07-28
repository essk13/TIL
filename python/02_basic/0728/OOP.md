# 객체지향 프로그래밍(Object Oriented Programing)

## 1. 객체(object)

- 클래스(class)에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것

- 객체는 특정 타입의 인스턴스 (object == instance)

  ```
  <예시>
  100, 95, 5 => int의 인스턴스
  'hello', 'bye' => str의 인스턴스
  [1, 2], ['a', 'b'] => list의 인스턴스
  ```

- **특징**

  - **타입(type)** : 어떤 operator와 method가 가능한가?
  - **속성(attribute)** : 어떤 data를 가지는가
  - **조작(method)** : 어떤 행위(함수)를 할 수 있는가?

- **속성 (attribute)**

  - \<object>.\<attribute>
  - 객체의 상태 / 데이터

- **메서드 (method)**

  - \<object>.\<method>( )
  - 특정 객체에 적용될 수 있는 행위 / 일반적으로 클래스에 정의된 함수

  |       Object       |       Class        |        Instance        |
  | :----------------: | :----------------: | :--------------------: |
  |    - 현실세계 -    |     - 출입구 -     |      - 가상세계 -      |
  | - 현실의 모든 것 - |     - 설계도 -     | - 가상세계의 모든 것 - |
  |     현실의 나      | 데이터, 행동 등을  |     가상세계의 나      |
  |         🤵          | 저장하기 위한 수단 |           🤵            |

## 2. 객체지향 프로그래밍 (OOP)

- **명령형 프로그래밍**

  - **절차지향 프로그래밍** : 데이터와 함수
  - **객체지향 프로그래밍** : 데이터와 메서드 분리, 추상화된 구조(인터페이스)

- **클래스와 인스턴스**

  - **클래스(class)** =  객체들의 분류
  - **인스턴스(instance)** = 하나하나의 객체
  - **속성(attribute)** = 인스턴스들이 가지는 상태 및 데이터
  - **메서드(method)** = 인스턴스가 적용 가능한 행위(함수)

  ```python
  class MyClass:            # class 정의
      pass
  my_instance = MyClass()   # 인스턴스 생성
  my_instance.my_method()   # 메서드 호출
  my_instance.my_attribute  # 속성
  ```

- **self**

  - 인스턴스 자기자신
  - 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되도록 설계

- **생성자 (constructor)**

  - **\__init__**

  - 인스턴스 객체가 생성될 때 호출되는 메서드

- **소멸자 (distructor)**

  - **\__del__**
  - 인스턴스 객체가 제거될 때 호출되는 메서드

- **매직 메서드**

  - Double underscore(__ / 던더스코어)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  - 스페셜 메서드 or 매직 메서드

  ```python
  __str__(self) # 객체의 출력 형태를 지정하는 메서드
  __repr__(self) # 프린팅 메서드 / 객체를 출력할 때 호출하는 메서드
  __len__(self), __lt__(self,other) etc...
  ```

## 3. 클래스와 인스턴스

- **인스턴스 변수**

  - 인스턴스 속성(attribute)

  - 각 인스턴스들의 고유한 변수

    ```
    self.<name> 으로 정의
    <instance>.<name>으로 접근
    ```

- **클래스 변수**

  - 클래스 속성(attribute)

  - 모든 인스턴스가 공유

    ```
    클래스 내부에서 정의
    <classname>.<name>으로 접근 및 할당
    ```

- 인스턴스와 클래스의 **namespace**

  - **namespace 탐색 순서**

    ​	**① instance 변수**

    ​	**② class 변수**

    ​	**③ global 변수**

    ```markdown
    	※ 인스턴스 변수가 클래스 변수에 접근해 변경하면 클래스 변수 변경 X
    	   해당 인스턴스 에 새로운 변수 생성 및 더 이상 클래스 변수 접근 불가
    ```

- **메서드의 종류**

  - **인스턴스 메서드**

    - 인스턴스가 사용할 메서드

      → 클래스에 영향 X, 독립적으로 행동

    - 클래스 내부에 정의되는 메서드의 기본

    - 호출 시, 첫 인자로 self 전달

      ```python
      class Myclass:
      	def instance_method(self, arg1, ...):
      	
      my_instance = MyClass()
      my_instance.instance_method(...)
      ```

  - **클래스 메서드**

    - 클래스가 사용할 메서드

      → 클래스의 변수에 접근 및 변경

    - @classmethod 데코레이터 사용하여 정의

    - 호출 시, 첫 인자로 클래스(cls) 전달

      ```python
      class Myclass:
          @classmethod
          def class_method(cls, arg1, ...):
           
      MyClass.class_method(...)
      ```

  - **스태틱 메서드(정적 메서드)**

    - 클래스가 사용할 메서드

    - @staticmethod 데코레이터 사용하여 정의

    - 호출 시, 어떠한 인자도 전달 X

      ```python
      class MyClass:
          @staticmethod
          def staticmethod()
       
      MyClass.staticmethod()
      ```

  - **메서드 정리**

    - 인스턴스는 모든 메서드 호출 가능 (할 수 있지만 하지 말 것!)
    - 클래스는 클래스 속성 접근 여부에 따라 클래스메서드 또는 스태틱 메서드 정의

## 4. 상속

- **상속**

  - 부모 클래스의 속성, 메서드를 상속 → 코드 재사용성 향상

    ```python
    class ChildClass(ParentClass):
    	pass
    ```

- **isinstance(object, classinfo)**

  - object가 classinfo의 instance 이거나 subclass인 경우 True 반환

- **issubclass(class, classinfo)**

  - class가 classinfo의 subclass인 경우 True 반환
  - classinfo는 튜플로 전달 가능 (모든 항목 검사)

- **super( )**

  - 자식클래스에서 부모클래스의 속성 및 메서드를 사용하려는 경우

- **메서드 오버라이딩**

  - 부모 클래스로 부터 상속 받은 메서드를 재정의하여 사용하는 것
  - 상속 받은 메서드를 그대로 사용하는 경우  super() 사용

- **다중상속**

  - 두개 이상의 부모클래스를 상속
  - 같은 이름의 변수에 접근 시 앞의 부모클래스를 먼저 탐색
