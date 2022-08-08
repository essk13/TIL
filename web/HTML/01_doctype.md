# DOCTYPE (DTD: Document Type Declaration)

## [정의] Doctype이란?

- **문서의 유형을 정의하기 위해 사용하는 선언문**
  
  - **HTML5, XHTML, HTML(HTML2 ~ HTML4)**
  
  ```textile
  1. DTD를 통해 현재 웹문서가 어떤 버전의 HTML 기술로 작성되었는지 브라우저에 전달
  2. 브라우저는 선언된 문서에 맞는 HTML 기술로 페이지 로드
  ```

## [목적] Doctype을 선언하는 이유

- **문서간 호환성을 높이기 위함 (과거와 현재)**
  
  ```textile
  1. 현재 기술의 웹표준과 과거의 웹표준이 일치하지 않기 때문에 오류 발생 가능
  2. 과거 버전의 문서들의 호환성을 유지하여 자료를 보존하기 위해 선언
  ```

- **모든 브라우저에서 같은 결과물을 보기 위함 (위와 연결)**
  
  ```textile
  1. Doctype 무선언 → 쿼크모드 렌더링 → 브라우저마다 다른 결과물 출력 가능
  2. Doctype 선언 → 표준모드 렌더링 → 브라우저 간 같은 결과물 출력
  ```

## [선언] Doctype 선언

- **HTML5 문서 선언**
  
  ```html
  <!DOCTYPE html>
  ```

- **XHTML1.0 문서 선언**
  
  - Strict (엄격모드: \<center>, \<font> 등 14가지의 태그 사용 금지)
    
    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    ```
  
  - Transitional (호환모드: 금지된 몇 가지 태그 사용 허용)
    
    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    ```
  
  - Frameset (프레임셋: 프레임 구조 지원)
    
    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
    ```

- **XHTML1.1 문서 선언** (엄격모드)
  
  ```
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
  ```

- **HTML4.01 문서 선언**
  
  - Strict (엄격모드: <center>, <font> 등 14가지의 태그 사용 금지)
    
    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    ```
  
  - Transitional (호환모드: 금지된 몇 가지 태그 사용 허용)
    
    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    ```
  
  - Frameset (프레임셋: 프레임 구조 지원)
    
    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
    ```



**[[참조] HTML5 v HTML4.0 v XHTML1.0 호환 모드별 허용 태그](https://dasima.xyz/doctype-html/#doctypetable)**
