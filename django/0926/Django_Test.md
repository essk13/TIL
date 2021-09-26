# Django_TEST

## 1. Django 기초 사용법

**※ 작성 순서 ※**

요청과 응답 흐름 순서대로 코드를 작성 및 수정

(**① urls.py => ② views.py => ③ templates**)



### ※ CRUD 정리 ※

#### 1) 가상환경 생성

```
$ python -m venv venv(가상환경 폴더명)
```

#### 2) 가상환경 실행

```
$ source venv/Script/activate
```

#### 3) 필수 파일 설치

```
$ pip install -r requirements.txt
```

#### 4) 장고 PJT 생성

```
$ django-admin startproject config(설정 폴더명) .(dot 미작성시 프로젝트 폴더, 설정폴더가 같이 생성)
```

#### 5) 장고 작동 확인

```
$ python manage.py runserver (주소로 이동하여 로켓 확인 / 종료 = ctrl + c)
```

#### 6) 애플리케이션 생성

```
$ python manage.py startapp article(APP명)
```

#### 7) settings.py / INSTALLED_APPS에 APP 추가

```python
INSTALLED_APPS = [
	'article(APP명)',
]
```

#### 8) 기본 setting 설정

```python
INSTALLED_APPS = [
	'library_name',
]
##############################################
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates']
    }
]
##############################################
STATIC_URL = '/static/'
STATIC_FILES = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
```

#### 9) base.html 생성

\- PJT Directory \ templates

```django
  <div class="container">
  {% block content %}
  {% endblock  %}
  </div>

{# 자식템플릿 최상단 {% extends 'base.html' %} 태그 작성 필수 #}
```

#### 10) urls.py / path 등록

```python
from article(APP명) import views

urlpatterns = [
	path('경로/', views.<function>),
]
```

#### 11) URL Mapping

**① 설정 폴더 / urls.py**

​		\- include() 함수 호출 및 APP.urls path 등록

​		**\- 이미지 업로드 구현 시 static 함수 정의 필요**

```python
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', include('articles.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**② APP 폴더 / urls.py**

​		\- 각 APP 폴더 내부에 urls.py 파일 생성

​		\- path()함수 및 views 모듈 호출

​		\- app_name 작성 및 urlpatterns 리스트 생성

​		\- path 마지막 인자로 path 명 지정

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    ...
]
```

- **URL Path converters**
  - 변수 저장 default = str
    - 지정 방법 : \<str:변수명> / \<int:변수명>/\<slug:변수명>
    - str = 문자열 / int = 0 또는 양의 정수 / slug = ASCII문자 또는 숫자, '-', '_' 로 구성된 모든 슬러그 문자열

#### 12) Model 정의 (models.py)

**이미지 업로드 구현 시 Pillow 라이브러리 설치 필수**

```python
from django.db import models

class Article(models.Model):	# 설계도(migration)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=Ture, upload_to='저장 경로')
    created_at = modles.DateTimeField(auto_now_add=Ture)
    updated_at = modles.DateTimeField(auto_now=Ture)
    
    def __str__(self):	# 개발자 및 사용자용 문자열 반환 기능
        return self.title
```

#### 13) makemigrations & migrate

```
# 모델 수정시 필수 #
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 14) admin 페이지 등록

\- 모델 import

\- 모델 관리자 class 생성 (선택)

\- 모델에서 \__str__ 메직 메서드로 관리자 페이지 출력명 설정 가능

\- 관리자 계정 생성 : $ python manage.py createsuperuser

```python
from django.contrib import admin
from .models import Article

# 모델 관리자 class를 통해 보다 상세한 관리자 페이지 설정 가능
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

admin.site.register(Article, ArticleAdmin)
```

#### 15) ModelForm 정의

\- App_Directory \ forms.py

```python
from django import forms
from .models import Article	# 상속받을 모델 호출

class Model_nameForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' 		   # 모든 field or 필요한 필드만 지정 가능
        # exclude = ('attribute',) # 제거 할 field
```

+)  Widget 적용

```python
class Model_nameForm(forms.ModelForm):
    attribute = forms.Field_type(
        (label='',)
        widgets=forms.TextInput(
            attrs={
                'class': '',
                'style': 'value'
            }
        )
    )
    class Meta:
        model = Model_name
        fields = '__all__'
```

##### **※ 주의 ※**

\-  \<APP>/templates/<파일명>.html

```
templates 폴더 위치, 폴더명 확인 필수※ 오류 시 Template Does Not Exist 오류 발생
```

#### 16) INDEX

\- 데코레이터 작성은 자율

**① view 함수**

```python
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

**② index.html**

```django
{% block content %}
  {% for article in articles %}
    <p>Attribute1 : {{ article.title }}</p>
  {% empty %}
	<p>No</p>
  {% endfor %}
{% endblock %}
```

#### 17) CREATE

\- 데코레이터 작성은 자율

**① view 함수**

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'btn_name': '작성'
    }
    return render(request, 'articles/form.html', context)
```

**② form.html**

\- CREAT, UPDATE 공유

```django
{% block content %}
  {# MEDIA 파일 업로드 구현 시 enctype 필수 #}
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button>{{ btn_name }}</button>
  </form>
{% endblock content %}
```

#### 18) DETAIL(READ)

\- 데코레이터 작성은 자율

**① view 함수**

```python
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

**② detail.html**

```django
{% block content %}
	중략
  {% if article.img %}
	{# 이미지 조회 시 .url 필요 #}
    <img src="{{ article.image.url }}" alt="{{ article.title }} image">
  {% endif %}
	중략
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button><a href="{% url 'articles:update' article.pk %}">수정</a></button>
    <button>삭제</button>
  </form>
{% endblock content %}
```

#### 19) UPDATE

\- 데코레이터 작성은 자율

**① view 함수**

```python
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'btn_name': '수정',
    }
    return render(request, 'articles/form.html', context)
```

**② form.html 공유**

#### 20) DELETE

\- 데코레이터 작성은 자율

**① view 함수**

```python
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')
```

#### 21) STATIC

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

---



### ※ Authentication 정리 ※

\- App 생성 및 URL Mapping 까지 동일

#### 0) views.py 에서 필요한 function, form 호출

```python
# login, logout 함수명 중복 방지 필수
from django.contrib.auth import ( login as auth_login,
                                  logout as auth_logout,
                                 )
from django.contrib.auth.forms import ( UserCreationForm,
                                        AuthenticationForm,
                                        PasswordChangeForm,
                                       )
from .forms import CustomUCF
```

#### 1) Signup

\- 데코레이터 작성은 자율

**① view 함수**

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

**② signup.html**

```django
{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>가입</button>
  </form>
{% endblock content %}
```

#### 2) Login

\- 데코레이터 작성은 자율

**① view 함수**

**※ 주의 ※**

\- AuthenticationForm은 ModelForm이 아님!!

\- 첫 인자 == request

\- form.save() 사용 불가

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # login 함수명 중복 주의
            auth_login(request, form.get_user())
            # next 쿼리스트링 수행여부 설정(선택사항)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

**② login.html**

```django
{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>로그인</button>
  </form>
{% endblock content %}
```

#### 3) Logout

\- 데코레이터 작성은 자율

**① view 함수**

```python
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
```

#### 4) DELETE (탈퇴)

\- 데코레이터 작성은 자율

**① view 함수**

\- logout 함수 사용 시 순서 주의

```python
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')
```

#### 5) UPDATE (정보수정)

\- 데코레이터 작성은 자율

**① form**

\- forms.py

\- 기본 UserChangeForm은 권한 외적인 부분까지 수정 가능함으로 커스텀 필요

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUCF(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
```

**② view 함수**

```python
def chg_user(request):
    if request.method == 'POST':
        form = CustomUCF(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUCF(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/chg_user.html', context)
```

**③ chg_user.html**

```django
{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>수정</button>
  </form>
{% endblock content %}
```

#### 6) chg_pw (비밀번호 수정)

\- 데코레이터 작성은 자율

**① view 함수**

```python
def chg_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/chg_pw.html', context)
```

**② chg_pw.html**

```django
{% block content %}
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>수정</button>
  </form>
{% endblock content %}
```

----



### + Decorator

```python
from django.views.decorators.http import ( require_POST, # POST 요청만 허용
                                           require_safe, # GET, HEAD 요청만 허용
                                           require_http_methods, # 지정 요청만 허용
                                          )
from django.contrib.auth.decorators import login_required # 인증 사용자만 허용
```

+) @login_required와 if request.user.is_authenticated: 차이

```
@login_required
 - 인증된 사용자만 기능 사용 가능
 - 로그인 페이지로 이동
 - next 파라미터로 다음 행동 지정
 - login view 함수에서 next 쿼리스트링 행동 수행 가능하도록 정의 필요
if request.user.is_authenticated:
 - 인증된 사용자만 기능 사용 가능
 - 부가 조건을 통해서 미인증 사용자 접근시 행동 정의 필요
```

----



### + Template / form 변수

**\- .as_p()**

​	· `<p>` 각 field `</p>`

**\- .as_ul()**

​	· `<li>` 각 field `</li>`

**\- .as_table()**

​	· `<tr>` 각 field `</tr>`

