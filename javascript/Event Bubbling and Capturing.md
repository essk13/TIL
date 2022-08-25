# 이벤트 버블링과 캡쳐링 (Bubbling & Capturing)

### 이벤트 버블링 (Event Bubbling)

- 특정 엘리먼트에 이벤트가 발생하면 해당 **엘리먼트의 조상들에게 이벤트가 까지 전달되는 현상**

- 예시)
  
  - div > ul > li 의 구조
  
  - click 이벤트 리스너 >> alert
    
    ```html
    <div>
      <ul>
        <li></li>
      </ul>
    </div>
    ```
    
    ```javascript
    $('li').addEventListener('click', alert('This is li event'))
    $('ul').addEventListener('click', alert('This is ul event'))
    $('div').addEventListener('click', alert('This is div event'))
    ```
  
  - li 태그 클릭 시 li 태그 이벤트 >> ul 태그 이벤트 >> div 태그 이벤트 순으로 전달 됨

- **타겟 엘리먼트 (Target Element)**
  
  - 최초로 이벤트를 발생시킨 엘리먼트 (예시의 li 태그)
  
  - **event.target**

### 이벤트 캡쳐링 (Event Capturing)

- 특정 엘리먼트에 이벤트가 발생하면 해당 엘리먼트의 **최상위 부모 엘리먼트로부터 이벤트가 전달되어 내려오는 현상**

- 캡쳐링 수행을 위해 이벤트 핸들러에 {capture: true} 또는 true 설정 (기본값 = false)

- 예시)
  
  - div > ul > li 의 구조
  
  - click 이벤트 리스너 >> alert
    
    ```javascript
    $('li').addEventListener('click', alert('This is li event'), {capture: true})
    $('ul').addEventListener('click', alert('This is ul event'), true)
    $('div').addEventListener('click', alert('This is div event'), true)
    ```
  
  - li 태그 클릭시 div 태그 이벤트 >> ul 태그 이벤트 >> li 태그 이벤트 순으로 전달 됨

### 버블링 및 캡쳐링 중단

- **event.stopPropagation()**
  
  - 버블링 : 타겟 엘리먼트의 이벤트만 발생
  
  - 캡쳐링 : 타겟 엘리먼트 기준 최상위 엘리먼트의 이벤트만 발생
  
  - 하나의 이벤트에 여러 핸들러가 존재하는 경우 다른 이벤트는 버블링 유지
    
    ```html
    <div>
      <ul>
        <li onclick="event.stopPropagation()"></li>
      </ul>
    </div>
    ```
    
    또는
    
    ```javascript
    $('li').click(function(event) {
      event.stopPropagation()
      alert('This is li event')
    })
    ```

- **event.stopImmediatePropagation()**
  
  - 캡처링과 버블링을 포함한 다른 모든 이벤트 핸들러 실행 중단

- **+) event.preventDefault()**
  
  - 태그의 고유 기능(동작) 중단
    
    ```javascript
    $('a').click(function(event){
        event.preventDefault();
        alert('This is e.preventDefault()');
    });
    ```


