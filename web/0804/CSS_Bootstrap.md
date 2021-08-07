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
       stretch
       baseline
       ```

         **\- align-self**

       ```
       flex-start, end / center
       stretch
       space-between
       space-around
       ```

         **\- algin-content**

       ```
       auto
       flex-start, end / center
       stretch
       baseline
       ```

     - 기타

         **\- flex-wrap**

         **\- flex-flow**

         **\- flex-grow**

         **\- order**

   - 

5. **Grid system**

## II. Bootstrap

