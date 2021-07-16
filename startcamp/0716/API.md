# API

- **API 란?**

  - 체제와 응용프로그램 사이의 통신에 사용되는 언어나 메시지 형식

  - 어떤 플렛폼이든 같은 정보를 수집 할 수 있게 해주는 시스템

    

    ![API](API.assets/API.png)

## Web Crawling

- **Web Crawling 이란?**

  - 조직적, 자동화된 방법으로 웹을 탑색하는 것.

  - 검색 엔진과 같은 여러 사이트에서는 데이터의 최신 상태 유지를 위해 웹 크롤링 실시

    

  <img src="API.assets/web crawling.png" alt="web crawling" style="zoom: 33%;" />

- **정보 스크랩**

  1. 정보가 있는 사이트 URL을 확인

     ```python
     # 원하는 주소로 요청, 응답 저장
     import requests
     response = requests.get(url).text
     # 정보를 출력 및 확인
     print(response)
     ```

  2. URL로 요청

     ```python
     # 정보를 조작하기 편하게 변환
     from bs4 import BeautifulSoup
     data = BeautifulSoup(response)
     # 바꾼 정보 중 원하는 것만 추출
     kospi = data.select_one('selector 경로')
     # 출력
     print(kospi.text)
     ```

  3. 응답 결과에서 원하는 정보 확인

- **requests 모듈**

  - 파이썬에서 서버에 요청할 때 사용하는 모듈 (기본 제공 모듈 X)

  - 설치방법

    ```
    $ pip install requests
    ```

  - 사용방법

    ```python
    # requests.get('URL')
    # 'URL'에 요청(requests) 해서, 정보를 받다(get)
    
    import requests
    
    requests.get('URL')
    requests.get('URL').text           # text 문서 형식으로 수신
    requests.get('URL').status_code    # 상태 코드만 추출
    requests.get('URL').json()         # json 형식으로 수신
    ...
    ```

- **beautifulsoup4 모듈**

  - 문서를 검색하기 좋게 만드는 모듈

  - 설치방법

    ```python
    $ pip install beautifulsoup4       # 설치
    from bs4 import BeautifulSoup      # 모듈 호출
    ```

  - 사용방법

    ```python
    BeautifulSoup(문서)
    BeautifulSoup.select(경로)          # 문서 안에 있는 특정 내용 추출
    BeautifulSoup.select_one(경로)      # 문서 안에 있는 특정 내용 하나만 추출
    
    # ex)
    data = BeautifulSoup(response)
    ```

- **JSON (JavaScript Object Notation)**

  - 데이터만을 주고 받기 위한 표기법
  - 파이썬의 Dictionary와 List 구조로 쉽게 변환하여 활용 가능

## API 활용

1. 정보가 있는 API URL을 확인

   ```
   url = 'https://abcd'
   ```

2. URL로 요청

   ```python
   response = requests.get(url).json()
   ```

3. 응답 결과를 확인 정보 출력

   ```python
   print(response)
   ```

   