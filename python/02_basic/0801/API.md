# API (Application Programming Interface)

## 1. Web

- 구성요소

  ```
  1) HTTP
  2) URL
  3) 웹문서
  ```

### HTTP (Hyper Text Transfer Protocol)

- **요청 (request)** - Client	>>	**응답(response)** - Server

  ```markdown
  # Request
  	Client	----- URL --->>	Server
  # Response
  	Server	-- 문서/Text ->> Client
  ```

### Requests (HTTP for Humans)

```
$ pip install requests
----------------------------
import reqeusts
response = requests.get('URL')  ## 요청
# => Response 200 # == 성공
print(response.text)  ## 문서화 출력
```

### Crawling

- 웹에서 정보를 모아오는 것

### Beautiful soup

```
$ pip install beautifulsoup4 (해석)
----------------------------
from bs4 import BeautifulSoup
data = BeautifulSoup(response.text, 'html.paser')
print(data.selct-one('copy seletor'))
```

## 2. API

- 응용 프로그램을 위한 접점

### API server

- 응용프로그램(개발자)를 위한 데이터 응답 프로그램

  ex) agify, TMDB Helper, NaverDeveloper etc..