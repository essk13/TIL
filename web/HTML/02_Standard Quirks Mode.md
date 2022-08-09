# 표준모드 (Standard mode)와 쿼크모드(Quirks mode)

## [정의] 표준모드와 쿼크모드란?

- **표준모드 (Standard mode)**
  
  - W3C 표준에 따라 렌더링

- **쿼크모드 (Quirks mode)**
  
  - 오래된 웹 브라우저의 행동을 모방하여 렌더링

## [이유] 렌더링 모드를 사용하는 이유

- **오래된 웹 페이지**의 경우 현재의 웹 표준과 일치하지 않아 **의도한 대로 출력되지 않는 문제 발생** → 이를 해결하기 위해 렌더링 모드 도입

## [방안] 렌더링 모드 선택 (오래된 문서 판단 기준)

- **Doctype Sniffing (Swiching)**
  
  - **DTD(Document Type Defination)** 을 기준으로 표준 또는 쿼크모드로 렌더링하는 과정
  
  - **DTD = PUBLIC 문자열 + FPI(Formal Public Identifier) + FSI(Formal System Identifier)**
  
  ```textile
  1. Doctype(DTD)에 FPI와 FSI가 동시에 기술되어 있는 경우 → Standard mode
      → <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd
  Viewer
  ">
  2. Doctype(DTD)에 FPI만 기술되어 있는 경우 → Quirks mode
      →  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
  3. Doctype이 선언되지 않은 경우 → Quirks mode
  ```

## [한 줄 정리]

- 오래된 웹 페이지를 최신 브라우저에서 깨지지 않고 의도대로 출력하기 위해서 Quirks mode를 사용한다.
