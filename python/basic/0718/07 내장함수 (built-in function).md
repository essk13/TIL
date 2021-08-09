# 내장함수 (built-in function)

- **내장함수란?**
  - 프로그램 언어의 라이브러리에 내장되어 있어서, 프로그램 작성자가 정의하지 않고 그대로 사용할 수 있는 함수

## 수치 연산 함수

- **abs( )**

  - 인자로 숫자를 전달하면 절대값을 반환하는 함수

    ```python
    abs(-2) = 2
    ```

- **divmod( )**

  - 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 튜플 객체로 반환하는  함수

    ```python
    divmod(19, 3) = (6, 1)
    ```

- **pow( )**

  - 첫번째 인자를 두번째 인자로 제곱한 결과를 반환하는 함수

    ```python
    pow(2, 2) = 4
    ```

## 시퀀스형 / 반복 가능한 자료형을 다루는 함수

- **all( )**

  - 반복 가능한 자료형(list, tuple 등)을 인자로 전달,

    항목 모두 Ture 이면 True 반환,  하나라도 False 이면 False를 반환하는 함수

    ```python
    list_a = [True, False]
    
    all(list_a) = False
    ```

- **any( )**

  - all( ) 함수의 반대

  - 반복 가능한 자료형(list, tuple 등)을 인자로 전달,

    항목 모두 Flase 이면 False 반환,  하나라도 True 이면 True를 반환하는 함수

    ```python
    list_a = [True, False]
    
    all(list_a) = True
    ```

- **enumerate( )**

  - 시뭔스형(list, tuple, 문자열)을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환하는 함수

    ```python
    
    ```

- **filter( )**

  - 조건에 해당하는 항목을 걸러내는 함수

  - 자료형 인자가 True 인 항목만 추출

    <img src="07 내장함수 (bilt-in function).assets/filter.PNG" alt="filter" style="zoom:50%;" />

    ```python
    def iseven(num):
        return num % 2 == 0
    
    numbers = range(1, 11)
    
    ret_val = filter(iseven, numbers)
    # ret_val = filter(lambda n : n % 2 ==0, numbers)
    list(ret_val) = [2, 4, 6, 8, 10]
    ```

- **list( )**

  - 리스트[ ]로 반환하는 함수

- **tuple( )**

  - 튜플( )로 반환하는 함수

- **set( )**

  - 셋{ }으로 반환하는 함수

- **dict( )**

  - 딕셔너리{key : value}로 반환하는 함수

- **map( )**

  - 두번째 인자로 반복 가능한 자료를 전달,

    자료형의 각 항목을 첫번째 인자로 전달 받은 함수를 적용한 결과를 '맵 객체'로 반환하는 함수

    ```python
    list_a = [1, 2, 3, 4, 5]
    
    list(map(str, list_a)) = ['1', '2', '3', '4', '5']
    ```

- **max( )**

  - 항목 중 가장 큰 값 반환하는 함수

- **min( )**

  - 항목 중 가장 작은 값 반환하는 함수

- **range( )**

  - 첫번째 인자를 시작값으로, 두번째 인자를 종료값으로, 세번째 인자를 증감치로 전달하여 시퀀스형 객체를 생성하는 함수

    ※ 두번째 인자는 범위에 포함되지 않음

    ```python
    # 첫번째 인자 기본값 = 0, 세번째 인자 기본값 = 1
    range(1, 10, 1) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

- **sorted( )**

  - 반복 가능한 자료형을 인자로 전달받아 항목들로 부터 정렬된 리스트를 생성해 반환하는 함수

  - 기본 - 오름차순, reversed( ) 중첩 - 내림차순

    ```python
    list_a = [3, 8, 12, 2, 5, 11]
    
    a = sorted(list_a) # = [2, 3, 5, 8, 11, 12]
    list(reversed(a))   # = [12, 11, 8, 5, 3, 2]
    ```

- **zip( )**

  - 둘 이상의 반복 가능한 자료형을 인자로 전달,

    동일 위치의 항목을 묶어 튜플을 항목으로 하는 zip 객체 생성하는 함수

    ※ 인자로 전달된 객체는 동일 자료형이면서 항목의 개수가 같아야 함

    ```python
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    
    dict(zip(list_a, list_b)) = {1: 'a', 2: 'b', 3:'c'}
    ```

## 변환 함수

- **chr( )**
  - 정수형의 유니코드 값을 인자로 전달, 해당 코드의 문자를 반환하는 함수
- **ord( )**
  - 문자를 인자로 전달, 유니코드 값(10진수)을 반환하는 함수
- **hex( )**
  - 10진 정수값을 인자로 전달, 16진수로 변환된 값을 반환하는 함수
- **int( )**
  - 숫자 형식 문자열과 부동소숫점 숫자를 정수로 반환하는 함수
- **float( )**
  - 숫자형식 문자열과 정수형을 부동소숫점 숫자로 반환하는 함수
- **str( )**
  - 객체를 문자열 반환값으로 전달하는 함수

## 객체 조사를 위한 함수

- **dir( )**

  - 객체가 가지고 있는 변수, 메서드와 같은 속성정보를 리스트 객체로 반환,

    인자 미전달 시 현재 지역 스코프에 대한 정보를 리스트 객체로 반환하는 함수

- **global( )**

  - 현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수

    ※ 전역변수와 함수, 클래스의 정보 포함

- **locals( )**

  - 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수

    ※ 매개변수를 포함한 지역변수와 중첩함수의 정보 포함

- **id( )**

  - 객체의 고유 주소(참고값)를 반환하는 함수

    ※ 고유 주소는 보통 16진수로 나타냄 → hex( )와 함께 사용

    ```python
    hex(id( ))
    ```

- **isinstance( )**

  - 첫번째 인자가 두번째 인자 클래스의 인스턴스인지를 True 또는 False로 반환하는 함수

- **issubclass( )**

  - 첫번째 인자가 두번째 인자의 클래스와 서브클래스인지를 True 또는 Flase로 반환하는 함수

    ```python
    class Parent:
    	pass
    
    class Child(Parent):
    	pass
    	
    p = Parent( )
    c = Child( )
    
    isinstance(p, Parent) = True
    insinsance(c, Parent) = True
    isinstance(p, Child) = False
    issubclass(Child, Parent) = True
    ```

## 실행관련 함수

- **eval( )**

  - 실행 가능한 표현식의 문자열을 인자로 전달, 해당 문자열의 표현식을 실행한 결과값을 반환하는 함수

    ```python
    expr = '2 + 5 * 3'
    expr2 = "'hello, python!'.upper()"
    
    eval(expr) = 17
    eval(expr2) = 'HELLO, PYTHON!'
    ```

    