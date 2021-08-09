# 모듈 (Module)

## 1. 모듈과 패키지

- **모듈**

  - 특정 기능을 파이썬 파일(.py) 단위로 작성한 것

- **패키지**

  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 내 서브 패키지 포함

- **라이브러리**

  - 패키지와 모듈들의 집합
  - **파이썬 표준 라이브러리 (Python Standard Library, PSL)**
    - 파이썬에 기본적으로 설치된 모듈과 내장 함수

- **pip (파이썬 패키지 관리자)**

  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 시스템

  - **명령어**

    ```markdown
    ※ git Bash, cmd 에서 사용
    
     - 설치 및 삭제
    
    $ pip install <somepakage> (최신버전 패키지 설치)
    $ pip install <somepakage> == <버전> (지정 버전 패키지 설치)
    $ pip install <somepakage> >= <버전> (지정 버전보다 최신 패키지 설치)
    	※ pip는 패키지 업그레이드 시 과거 버전 자동삭제
    $ pip uninstall <somepakage> (패키지 제거)
    
     - 패키지 목록, 정보, 관리
    
    $ pip list (설치된 패키지 목록 보기)
    $ pip show <somepakage> (특정 패키지 정보 보기)
    $ pip freeze (설치된 패키지 목록 생성)
    	$ pip freeze > requirements.txt (설치된 패키지 목록 txt 파일 생성)
    	$ pip freeze -r requirements.txt (패키지 목록 설치)
    	※ pip freeze 목록은 관습적으로 requirements.txt로 저장
    ```

- 모듈 사용법

  ```python
  1. import <module>
  2. from <module> import <var>, <function>, <class>
  3. from <module> import *
  
  4. from <package> import <module>
  5. from <package.module> import <var>, <function>, <class>
  ```

## 2. 가상환경

- **가상환경**

  - 복수의 PJT 진행 경우 외부 패키지 or 모듈의 버전이 다를 수 있음

    → 가상환경을 만들어 프로젝트 별로 독립적인 패키지 관리 가능

- **venv**

  - 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 3.5 이상 공식 모듈)

  - 특정 디렉토리에 가상환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음

    ```markdown
     - 생성
    $ python -m venv venv (해당 디렉토리에 별도의 파이썬 패키지 설치)
    
     - 활성화/비활성화
    $ venv/Script/activate.bat (Window 가상환경 활성화)
    	※ (venv) 표시 확인
    $ deactivate (가상환경 비활성화)
    
    	※ venv 폴더별로 고유한 프로젝트가 설치
    	   복사, 이동 금지
    ```

    

