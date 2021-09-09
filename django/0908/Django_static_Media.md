# Django Static / Media

## 1. Static files

- **Static file**

  - **정적 파일**

    - 개발자가 사용자에게 제공하는 파일
    - 이미지, JS(java script), CSS 등
    - 별도의 처리 없이 원본 파일 제공
    - 서전 설정 없이 파일 호출 시 미작동

  - **구성**

    **① settings.py 기본 설정**

    ```python
    INSTALLED_APPS =[
        'django.contrib.staticfiles',
    ]
    STATIC_URL = '/static/'
    ```

    **② App 폴더 내부 static 폴더 생성 및 static file 저장**

    ```
    App_Directory\static\app_name\static_file
    ```

    **③ static 로드 및 static file 호출**

    ```django
    {% load static %}
    
    {% static '경로(app_name/static_file)' %}
    ```

    **④ PJT 폴더 내부 static 폴더 생성 및 static file 저장**

    ```
    PJT_Directory\static\static_file
    ```

    **⑤ settings.py PJT 공통 static 경로 설정**

    ```python
    STATICFILE_DIRS = [BASE_DIR / 'static']
    ```

    **⑥ 배포를 위한 settings.py 설정** (설정 후 ⑦번 필수 수행)

    ```python
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```

    **⑦ 정적 파일을 수집하는 절대 경로 생성**

    ```
    $ python manage.py collectstatic
    ```

## 2. Media file

- **Media file**

  - **사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)**
  - 사전 설정 없이 작동 불가

- **Media Field**

  - **ImageField**

    - 이미지 업로드에 사용하는 모델 필드
    - FileField  상속 / 업로드 **객체가 유효한 이미지인지 검사**
    - **DB에 경로**가 max_length=100인 문자열로 **저장**
    - 원본 이미지는 DB가 아닌 Directory 경로에 저장
    - **blank 속성**을 통해 빈 문자열 허용여부 설정
    - **Pillow 라이브러리 설치 필수**

  - **FileField**

    - 파일 업로드에 사용하는 모델 필드

    - 2개의 선택인자 존재

      ​	**\- upload_to**

      ​			⊙ **upload Directory와 파일 이름을 설정**하는 방법 제공

      ​					**1) 문자열 값 또는 경로 지정**

      ```python
      class Model_name(models.Model)
      	# MEDIA_ROOT/uploads/ 경로로 파일 업로드
      	upload = models.FileField(upload_to='uploads/')
      	# MEDIA_ROOT/uploads/Year/Month/Day/ 경로로 파일 업로드
      	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
      ```

      ​					**2) 함수 호출**

      ​							\- 2개의 인자(instance, filename) 사용

      ​							**\- instance**

      ​									\- FileField가 정의된 모델의 인스턴스

      ​									\- DB에 저장되지 않아 PK값이 없는 경우 존재

      ​							**\- filename**

      ​									\- 기존 파일에 제공된 파일명

      ```python
      def articles_image_path(instance, filename):
          # MEDIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
          return f'user_{instance.user.pk}/{filename}'
      class Model_name(models.Model):
          upload = models.FileField(upload_to=articles_image_path)
      ```

      ​	\- storage

  - **구성**

    - **Media file 저장 경로 및 url 설정**

      ```python
      # settings.py
      MEDIA_ROOT = BASE_DIR / 'media'		# 저장경로
      MEDIA_URL = '/media/'				# 요청 url
      ```

    - **upload_to 속성 정의 (MEDIA_ROOT 하위 경로)**

      ```markdown
      # 선택사항
      1. 문자열 or 함수호출 방식으로 Field의 upload_to 속성 정의
      ```

    - **uploaded Image 호출**

      ```django
      <img src="{{ app_name.image(img).url }}" alt="{{ app_name.image(img) }}">
      ```

    - **PJT urls.py 설정**

      ```python
      from django.conf import settings
      from django.conf.urls.static import static
      
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

  - **CREATE(업로드)**

    - **form 태그 enctype(인코딩타입) 및 input 태그 accept 속성 정의**

      ```django
      <form action="{% url '' %}" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button></button>
        or <input type="submit" accept="image/*">
      </form>
      ```

    - **view 함수에서 FILES 객체로 수신**

      ```python
      def create(request):
          if request.method == 'POST':
              form = Model_nameForm(request.POST, request.FILES)
              # data=request.POST(첫번째 위치인자)
              # files=request.FILES(두번째 위치인자)
          ...
      ```

  - **UPDATE(수정)**

    - **view 함수에서 FILES 객체로 수신**

      ```python
      def update(request, pk):
          app_name = get_object_or_404(Model_name, pk=pk)
          if request.method == 'POST':
              form = Model_nameForm(request.POST, request.FILES, instance=app_name)
              # data=request.POST(첫번째 위치인자)
              # files=request.FILES(두번째 위치인자)
          ...
      ```

      

