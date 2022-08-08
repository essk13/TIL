# CSS & Bootstrap

## I. CSS Layout

1. **Display**

   | Display      | Description                                                  |
   | ------------ | ------------------------------------------------------------ |
   | block        | 줄 바꿈이 일어나는 요소 / 화면 크기 전체의 가로 폭 차지 / inline 포함 가능 |
   | inline       | 줄 바꿈이 일어나지 않는 행의 일부 요소 / content 너비만큼 폭 차지 / margin-r,l 만 지정 가능 |
   | inline-block | block과 inline의 특징 모두 존재 / 한 줄 표시 가능 / margin, width, height 지정 가능 |
   | none         | 해당 요소를 표시 X / 공간도 제거 / (visibility: hidden = 공간은 존재, 요소 표시 X) |

   **Block & Inline elements 수평 정렬**

   |                                  block |   sort   | inline              |                                                   |
   | -------------------------------------: | :------: | :------------------ | ------------------------------------------------- |
   |                    margin-right: auto; | 좌측정렬 | text-algin: left;   |                                                   |
   |                     margin-left: auto; | 우측정렬 | text-algin: right;  |                                                   |
   | margin-right: auto; margin-left; auto; | 중앙정렬 | text-algin: center; | ------------------------------------------------- |

2. **Position**

   - **static (기준 위치)** 
     - 모든 태그의 기본값(기준 위치)
     - 좌측상단, 부모 요소 내 배치되는 경우 부모 요소의 위치를 기준으로 배치
     - static 외는 top, bottom, left, right를 사용하여 이동 가능
   - **relative (상대위치)**
     - 자신의 static을 기준으로 이동 / 레이아웃에서 차지하는 공간은 static과 동일
   - **absolute (절대 위치)**
     - 가장 가까운 부모/조상 요소를 기준으로 이동(없는 경우 body를 기준) / 레이아웃에서 공간을 차지하지 않음
   - **fixed (고정 위치)**
     - viewport를 기준으로 이동(스크롤 시에도 같은 곳에 위치) / 레이아웃에서 공간을 차지하지 않음
   - **sticky (부모영역 고정 위치)**
     - 부모 영역을 기준으로 이동(스크롤 시 부모의 영역까지 viewport에 존재) / 레이아웃에서 공간을 차지

3. **Float**

   - 이미지 좌, 우측에 텍스트로 둘러싸는 레이아웃을 위해 도입

     → 다른 요소들에게도 적용해 웹 사이트 전체 레이아웃을 만드는 display로 발전

     → 현재는 이전의 역할로 회귀 / 여전히 사용되는 경우가 있음

     **※ float 시 레이아웃 상 위치를 가지지 않음 ※**

   - **속성**

       \- none : 기본값

       \- left : 요소를 좌측 정렬

       \- right : 요소를 우측 정렬

   - **Float clear (가상요소)**

     ```css
     .clearfix::after {
     	content: "";
     	disblay: block;
     	clear: both;
     }
     ```

       \- 선택한 요소의 마지막 자식으로 가상 요소를 생성 (기본값 = inline)
     
       \- 보통 content 속성과 함께 사용 / 장식용 콘텐츠를 추가할 때 사용

4. **Flexbox**

   - 구성요소

     - **Flex Container (부모 요소)**

         \- flexbox 레이아웃 형성의 가장 기본적인 모델

         \- flex item들이 놓이는 영역

         **\- display 속성 = flex / inline-flex**

       ​	**※ 부모 요소에 flex 작성 ※**

     - **Flex Item (자식 요소)**

         \- 컨테이너의 컨텐츠

   - 축

     - **main axis (메인축)**
     - **cross axis (교차축)**

   - 속성

     - **배치 방향**

         **\- flex-direction (메인축)**

       ```markdown
       	row(default)	우 → 좌
       	row-reverse		좌 → 우
       	column			상 → 하
       	column-reverse	하 → 상
       ```

     - **메인축 방향 정렬 (justify)**

         **\- justify-content**

       ```
       flex-start, end / center
       space-between
       space-around
       space-evenly
       ```

     - **교차축 방향 정렬 (align)**

       **\- align-items**

       ```1
       flex-start, end / center
       stretch = 컨테이너를 가득 채움(default)
       baseline
       ```

         **\- align-self**

       ```
       auto (default)
       flex-start, end / center
       stretch = 부모 컨테이너에 자동으로 맞춰서 늘어남
       space-between
       space-around
       ```

         **\- algin-content**

       ```
       auto
       flex-start, end / center
       stretch = 컨테이너를 가득 채움(default)
       baseline
       ```

         \- content = 여러 줄

         \- items = 한 줄

         \- self = 개별 요소

     - 기타

         **\- flex-wrap** : 허용량을 벗어나면 강제로 한 줄 배치할지 또는 줄을 바꿔 배치할지 결정

          					   \- nowrap(default)

          					   \- wrap

          					   \- wrap-reverse : 넘치면 윗줄로
         
         **\- flex-flow** : flex-direction과 flex wrap을 한 번에 설정하는 shorthand
         
         **\- flex-grow** : 주축에서 남은 공간을 항목에게 분배
         
         **\- order** : 항목이 나타날 순서 지정(1 = default)


## II. Bootstrap

1. **CSS library**

   - **spacing**

       \- html 텍스트 기본 사이즈는 16px

     

   - **color**

     

   - **Text**

       \- text-start, center, end

       \- text-decoration-none

       \- fw-bold, normal, light

       \- fst-italic

   - **Components**

       \- Bootstrap에서 제공하는 컨텐츠

   - **Flexbox in Bootstrap**

       \- d-flex

       \- justify-content-center

       \- align-items-center

   - **Responsive Web**

       \- 반응형 웹 (디바이스의 viewport에 따라 보이는 화면이 다르게 구성)

       \- 웹에 대한 접근 방식

2. **Grid System**

   - flexbox로 제작

   - **container, rows, column**으로 컨텐츠 배치 및 정렬

   - **12개 column / 6개 grid breakpoints**

   - **row**

       \- column의 wrapper

   - **column**

       \- content는 column에 존재

       \- row의 자식 == column

   - **breakpoints**

       \- 뷰포트 크기에서 반응형 레이아웃이 작동하는 방식을 결정하는 사용자 지정 가능한 너비

   - **offset**

       \- 지정한 만큼의 column 공백 설정

   - **nesting** (중첩)

