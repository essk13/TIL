# Django Library

## 1. Django-Imagekit

- **이미지 크기 변경** 라이브러리

  - 원본 이미지를 서버에 업로드하는 작업은 서버에 부담이 큰 작업
  - 원본 이미지의 사이즈를 조정하여 저장하거나 원본과 조정 이미지를 함께 저장하도록 도와주는 라이브러리

- 사용방법

  **① django-imagekit 설치**

  ```
  $ pip install dango-imagekit
  ```

  **② INSTALLED_APPS \ 라이브러리 추가**

  ```python
  # settings.py
  INSTALLED_APPS = [
  	'imagekit',
  ]
  ```

  **③ model 정의**

  ```python
  # models.py
  '''
  원본 및 썸네일 이미지 동시 저장
  '''
  from imagekit.models import ImageSpecField
  from imagekit.processors import Thumbnail
  
  image = ImageField(blank=True, upload_to='경로')
  img_thumb = ImageSpecField(
  	source='image',
      processors=[Thumbnail('w_size', 'h_size')],
      format='이미지형식',
      options={
          'quality': 1 ~ 100,
      }
  )
  ```

## 2. Django-Cleanup

- DB 삭제 시 해당 경로에 저장된 업로드파일 삭제 라이브러리

- 사용방법

  **① django-cleanup 설치**

  ```
  $ pip install django-cleanup
  ```

  **② INSTALLED_APPS \ 라이브러리 추가**

  ```python
  INSTALLED_APPS = [
      'django_cleanup',
  ]
  ```

## 3. Message Framework

- 1회성 메시지 표시

- 사용방법

  **① default 설정 확인**

  ​		\- settings.py \ INSTALLED_APPS, MIDDLEWARE, TEMPLATES

  **② MESSAGE_STORAGE 정의**

  ```python
  # settings.py
  MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
  # 'django.contrib.messages.storage.session.sessionStorage'
  ```

  **③ TAG 별 반환 값 변경**

  ```python
  # settings.py
  from django.contrib.messages import constants as messages
  MESSAGE_TAGS = {
      messages.INFO: '변경할 값',
      # Tag 종류
      # DEBUG, INFO, SUCCESS, WARNING, ERROR
  }
  ```

  **④ view 함수 내부에서 메시지 생성 및 반환**

  ```python
  # views.py
  from django.contrib import messages
  
  # 정석
  messages.add_message(request, messages.INFO, 'Hello world.')
  # short hand
  messages.debug(request, '%s SQL statements were executed.' % count)
  messages.info(request, 'Three credits remain in your account.')
  messages.success(request, 'Profile details updated.')
  messages.warning(request, 'Your account expires in three days.')
  messages.error(request, 'Document deleted.')
  ```

  **⑤ Template에서 표시** (Bootstrap alert 사용가능)

  ```django
  {% if messages %}
  <ul class="messages">
      {% for message in messages %}
      <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
      {% endfor %}
  </ul>
  {% endif %}
  ```

## 4. Paginator

- INDEX에 데이터가 너무 많은 경우 페이지로 분할하여 페이지당 일정 개수의 데이터만 표시하는 기능

- 사용 방법

  **① view 함수 에서 paginator 정의**

  ```python
  # views.py
  from django.core.paginator import Paginator
  
  def index(request):
      articles = Article.objects.all()
      paginator = Paginator(articles, '표시할 데이터 수')
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      context = {
          # 'articles': articles,
          'page_obj': page_obj,
      }
      return render(request, 'articles/index.html', context)
  ```

  **② Temaplate에서 정의한 데이터 수 표시**

  ```django
  {% for contact in page_obj %}
      {# Each "contact" is a Contact model object. #}
      {{ contact.full_name|upper }}<br>
      ...
  {% endfor %}
  ```

  **③ paignator 생성**

  ```python
  <div class="pagination">
      <span class="step-links">
          {% if page_obj.has_previous %}
              <a href="?page=1">&laquo; first</a>
              <a href="?page={{ page_obj.previous_page_number }}">previous</a>
          {% endif %}
  
          <span class="current">
              Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
          </span>
  
          {% if page_obj.has_next %}
              <a href="?page={{ page_obj.next_page_number }}">next</a>
              <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
          {% endif %}
      </span>
  </div>
  ```

  **④ Bootstrap-v5 활용**

  ```django
    <div class="d-flex justify-content-center">
      {% bootstrap_pagination page_obj pages_to_show=5 %}
    </div>
  ```

  