# Django REST Framework

## 1. HTTP (Hyper Text Transfer Protocol)

- 웹 상에서 컨텐츠를 전송하기 위한 약속

- HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜 (규칙, 약속)

- 특성

  ​	\- **쿠키**와 **세션**을 통해 서버 상태를 요청과 연결 실시

  ​	**\- Stateless**

  ​	**\- Connectless**

  **1) 요청(Request)** : Method / Path / Version of Protocol / Headers

  **2) 응답(Response)** : Version of the protocol / Status code / Status message / Headers

  

- **HTTP request methods**

  ​	\- 주어진 리소스(자원)에 수행하길 원하는 행위

  ​	ex) GET, POST, PUT, DELETE

  

- **HTTP response status codes**

  ​	1) Informational responses (1XX)

  ​	2) Successful responses (2XX)

  ​	3) Redirection messages (3XX)

  ​	4) Client error responses (4XX)

  ​	5) Server error responses (5XX)

  

- **웹에서 리소스 식별**

  ​	**\- 리소스(자원) = HTTP 요청의 대상**

  ​	\- 리소스 식별은 URI로 식별

  

- **URI (Uniform Resource Identifier)**

  ​	\- 통합 자원 식별자

  ​	\- 인터넷 레소스를 식별하는 유일한 주소

  ​	**\- 일반적으로 URL과 URI를 같은 의미로 사용하기도 함**

  - **URL (Uniform Resource Locator)**

    ​	\- 통합 자원 위치 (웹주소, 링크)

    ​	\- 과거 : 실제 자원의 위치 / 현재 : 추상화된 의미론적 구성

  - **URN (Uniform Resource Name)**

    ​	\- 통합 자원 이름

    ​	\- 자원의 위치에 영향을 받지 않는 유일한 이름 역할

  - **URI 구조**

    ​	\- https://www.example.com:80/path/to/myfile.html/?key=value#quick-start

    - **1) Scheme (protocol)**

      ```markdown
      # https://
      - 브라우저가 사용하는 프로토콜
      - http(s), data, file, ftp, malito ... etc
      ```

    - **2) Host (Domain name)**

      ```markdown
      # www.example.com
      - 요청을 받는 웹 서버의 이름
      - IP Address 직접 사용 가능
      ```

    - **3) Port**

      ```markdown
      # :80
      - 리소스 접근에 사용되는 기술적인 문(gate)
      - HTTP 프로토콜의 표준 포트 : HTTP 80, HTTPS 443
      ```

    - **4) Path**

      ```markdown
      # /path/to/myfile.html
      - 웹 서버상의 리소스 경로
      - 과거 : 실제 파일이 위치한 물리적 위치 / 현재 : 추상화 형태의 구조
      ```

    - **5) Query (Identifier)**

      ```markdown
      # /?key=value
      - Query String Parameters
      - 웹 서버에 제공되는 추가적인 매개 변수
      - & 로 구분되는 **Key-value** 목록
      ```

    - **6) Fragment (Fragment identifier)**

      ```markdown
      # #quick-start
      - Anchor
      - 리소스 내 북마크의 한 종류
      - 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
      - '#' 뒤의 부분은 요청시 서버에 전달하지 않음
      ```

      

## RESTful API

- **API (Application Programming Interface)**

  ​	\- 프로그래밍 언어가 제공하는 기능을 수행할 수 있도록 만든 인터페이스

  ​	\- 응답 데이터 타입 : HTML, XML, JSON ... etc

  

- **REST (Representational State Transfer)**

  ​	\- 소프트웨어 설계 방법론 / 네트워크 구조 원리의 모음

  - REST의 자원과 주소 지정 방법
    - **자원 : URI**
    
    - **행위 : HTTP Method**
    
    - **표현 : JSON으로 표현된 데이터**
    
      

- **JSON (JavaScript Object Notation)**

  ​	\- JavaScript의 표기법을 따른 단순 문자열

  - 특징

    ​	\- 사람이 읽고, 쓰기 쉽고 기계가 파싱하고 생성하기 쉬움

    ​	\- 프로그래밍 언어가 갖고 있는 자료구조로 쉽게 변화 가능 (**key-value 형태**)

    ​			\- Python : dictionary, JavaScript : object 등



- 
