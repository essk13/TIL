# Django Form 02

### 1. get_object_or_404( )

- **`get()` 호출** 후 예외(찾는 값이 없는 경우) 발생 시 500(DoesNotExist) 에러가 아닌 **404(PageNotFound)에러 발생**

- 상황에 따른 적절한 예외처리를 통해 **사용자에게 올바른 에러 전달**

- 조건 작성 시 **하나의 object만 탐색**할 수 있는 조건 설정

  ```
  get_object_or_404(Model_name, 조건)
  ```

### 2. Decorator

- 함수를 수정하지 않고 기능을 연장해주는 함수

- **Allowed HTTP method**

- 허용되지 않은 메서드 사용 시 405(MeothodNotAllowed) 에러 발생

  ```python
  from django.views.decorators.http import method_name
  ```

  - **require_http_method**
    - **인자로 허용 할 method 전달**
    - ex) require_http_method(['GET', 'POST'])
  - **require_http_POST**
    - POST 메서드만 허용
  - **require_http_safe**
    - GET, HEAD 메서드만 허용
  - require_http_GET
    - GET 메서드만 허용 / 미권장

