# CSS 변형속성 활용

### 1. Vender Prefix

- 표준이 확정되지 않은 CSS3 속성 사용시 작성하는 특별한 접두사
  - -webkit- : chrome, safari
  - -moz- : firefox

### 2. 변형속성

- 스타일 속성값의 변화를 통해 애니메이션 효과를 구현

  1. 위치 / 크기

     \- top, left, bottom, right, width, height

  2. 박스

     \- margin, padding, border-width, border-radius, boder-color

  3. 색상

     \- color, background-color, opacity

- 대상 속성, 시간, 수치변형함수, 지연시간 등을 지정할 수 있는 속성들로 구성

  \- transition : transition 속성을 한 번에 지정

  \- transition-property : 변형할 속성 지정

  \- transition-duration : 변형에 소요되는 시간 지정

  \- transition-timing-function : 수치 변형함수 지정 / default = ease

  \- transition-delay : 변형효과 지연시간 지정

