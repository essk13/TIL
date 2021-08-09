# 데이터 구조(DATA Structures)

## 1. 데이터 구조

- 데이터에 편리하게 접근하고, 변경하기 위해 데이터를 저장하거나 조작하는 방법
- 순서가 있는 데이터 구조(**Sequence**)
  - **문자열(String)**
  - **리스트(List)**
- 순서가 없는 데이터 구조(**Non-Sequence**)
  - **세트(Set)**
  - **딕셔너리(Dictionary)**

## 2. 문자열(String)

- 문자들의 나열

- **특징**

  ```
  1) Immutable
  2) ordered
  3) iterable
  ```

- **문자열 인덱스(index) & 자르기(Slicing)**

  - 문자열은 index를 통해 접근할 수 있음

    ```markdown
    x = [1, 2, 3]
    	 0, 1, 2 = index
    	-3,-2,-1 = index
    ```

  - 문자열은 index를 활용하여 자를 수 있음

    ```markdown
    x[start:stop:step] *(range() 함수를 생각하면 쉬움)
    	start = 시작할 index
    	stop  = 마지막으로 포함될 index + 1
    	step  = 생략 시 1
    ```

- **메소드(method)**

  \- 문자열 조회/탐색

  ```markdown
  .find(x)
  	첫번째 x의 index 반환 / 없으면 -1 반환
  .index(x)
  	첫번째 x의 index 반환 / 없으면 ValuError
  ```

  \- 문자열 변경

  ```markdown
  .replace(old, new [, count])
  	old를 new로 변환해서 반환 / count 지정 = count만큼만 실행
  .strip([chars])
  	특정 문자 제거(양쪽 / 왼쪽(l) / 오른쪽(r)) /	생략 시 공백 제거
  .split([chars])
  	특정 문자로 나눠서 리스트로 반환 / 생략 시 공백으로 나눔
  'separator'.join([iterable])
  	iterable 컨테이너 요소들을 구분자로 합쳐서 문자열로 반환
  .capitlize()
  	앞글자 대문자화
  .title()
  	앞글자, ' 또는 공백 이후 첫 문자 대문자화
  .upper()
  	대문자화
  .lower()
  	소문자화
  .swapcase()
  	대, 소문자 변환
  ```

  \- 문자열 검증

  ```markdown
  .isalpha()
  	알파벳 문자 여부 반환(유니코드상 letter)
  .isupper()
  	대문자 여부 반환
  .islower()
  	소문자 여부 반환
  .istitle()
  	타이틀 형식 여부 반환
  .isdecimal < .isdigit < .isnumeric
  ```

## 3. 리스트

- **특징**

  ```
  1) mutable
  2) ordered
  3) iterable
  ```

- **메소드(method)**

  \- 값 추가 및 삭제

  ```markdown
  .append(x)
  	리스트에 값 추가
  .extend([iterable])
  	리스트에 iterable 항목 추가
  .insert(i, x)
  	index(i) 위치에 값 추가
  .remove(x)
  	값이 x인 항목 제거
  .pop(i)
  	index(i) 위치의 항목 제거 및 반환
  .clear()
  	모든 항목 제거
  ```

  \- 탐색 및 정렬

  ```markdown
  .index(x)
  	x값을 찾아 index 반환 / 없으면 ValueError
  .count(x)
  	원하는 값의 개수 반환
  .sort()
  	원본 리스트 정렬 / None 반환
  	※ sorted() 함수와 비교 - sorted()는 원본 유지 / 새로운 리스트 반환
  .reverse()
  	원본 리스트 순서를 뒤집음 / None 반환
  ```

  \- 리스트 복사

  ```markdown
  shallow copy(얕은 복사)
  	1) Slice 연산자 사용
  	2) list() 함수 사용
  	※ 주의 ※
  	리스트의 항목이 주소를 참조하는 경우[ex) 2중 리스트] 해당 값은 복사X
  deep copy(깊은 복사)
  	improt copy / copy.deepcopy(list)
  	※ 리스트의 항목이 주소를 참조하는 경우에도 복사 가능
  ```

  \- List Comprehension

  ```python
  # 표현식과 제어문을 통해 특정한 값을 가진 리스트를 생성하는 방법
  # 이중 반복문 등 다양한 문법으로 활용 가능
  [<expression> for <변수> in <inerable>]
  [<expression> for <변수> in <inerable> if <조건식>]
  ```

  \- Built-in Function

  ```markdown
  map(function, iterable)
  	iterable 데이터 구조의 모든 항목에 함수를 적용 / map 객체 반환
  filter(function, iterable)
  	iterable 데이터 구조의 모든 항목에 대한 결과가 True인 항목만 반환 / filter 객체 반환
  zip(*iterables)
  	복수의 iterable을 모아 튜플 원소로 반환 / zip 객체 반환
  ```

## 4. 세트

- **특징**

  ```
  1) mutable
  2) unordered
  3) iterable
  ```

- **메소드(method)**

  ```markdown
  .add(elem)
  	세트에 값 추가
  .update(*others)
  	여러 값을 추가
  .remove(elem)
  	항목 제거 / 없으면 KeyError
  .discard(elem)
  	항목제거 / 없어도 Error 미발생
  .pop()
  	임의의 항목을 랜덤하게 제거 및 반환
  ```

## 5. 딕셔너리

- **특징**

  ```
  1) mutable
  2) unordered
  3) iterable
  ```

- **메소드(method)**

  \- 조회

  ```markdown
  .get(key[, default])
  	key에 대응하는 value 반환 / key가 없으면 default 반환(생략시 None 반환)
  ```

  \- 추가 및 삭제

  ```markdown
  .pop(key[, default])
  	key에 대응하는 value 제거 및 반환 / key가 없으면 default 반환(생략시 KeyError)
  .update(key, value)
  	제공하는 값을 key, value로 덮어씀
  ```

  \- 딕셔너리 순회

  ```markdown
  .keys()
  	key로 구성된 결과 반환
  .values()
  	value로 구성된 결과 반환
  .items()
  	(key, value)로 구성된 결과 반환
  ```

  \- Dictionary Comprehension

  ```python
  # 이중 반복문 등 다양한 문법으로 활용 가능
  {key: value for <변수> in <iterable>}
  {key: value for <변수> in <iterable> if <조건식>}
  ```