# Django_03

## CRUD

### 1. CREATE

- 2개의 view 필요

  - **new (views.py)** : 작성페이지를 render 하는 view

    ```python
    def new(request):
        return render(request, 'articles/new.html')
    ```

    **new (new.html)**

    ```django
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>NEW</h1>
      <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}    
        <label>TITLE:
          <input type="text" name="title">
        </label>
    	<br>
        <label>CONTENT:<br>
          <textarea name="content"cols="29" rows="10"></textarea>
        </label>
        <br>
        <button class="btn btn-secondary py-0">WRITE</button>
        <a href="{% url 'articles:index' %}" class="text-decoration-none btn btn-secondary py-0">
        BACK
        </a>
      </form>
    {% endblock content %}
    ```

  - **create (views.py)** : 입력 데이터를 save 하는 view

    ```python
    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        pk = article.pk
        return redirect('articles:detail', pk)
    ```

### 2. READ

- **전체 요소**

  - **Article.objects.all()**

  - **index (views.py)**

    ```python
    def index(request):
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return render(request, 'articles/index.html', context)
    ```

    **index (index.html)**

    ```django
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>INDEX</h1>
      <a href="{% url 'articles:new' %}" class="text-decoration-none btn btn-secondary py-0">NEW</a>
      <hr class="border border-dark border-2">
      <div class="mt-3">
        {% for article in articles %}
          <h2>제목 : {{ article.title }}</h2>
          <p>내용 : {{ article.content }}</p>
          <a href="{% url 'articles:detail' article.pk %}" class="text-decoration-none btn btn-secondary py-0">DETAIL</a>
          <hr>
        {% empty %}
          <h1>등록된 게시물이 없습니다.</h1>
          <hr>
        {% endfor %}
      </div>
    {% endblock content %}
    ```

- **개별요소 (pk로 접근)**

  - **Article.objects.get(lookup)**

    ​	\- 값이 없거나 2개 이상인 경우 예외(에러) 발생

    ​	\- 유일한 값만 탐색 가능

    ​	**\- \<object> 반환**

  - **Article.objects.filter(lookup)**

    ​	\- 새로운 QuerySet 반환

    ​	\- 예외(오류) 미발생

  - **detail (views.py)** : "GET" 을 이용한 요청

    ```python
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            'article': article
        }
        return render(request, 'articles/detail.html', context)
    ```

    **detail (detail.html)**

    ```django
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>DETAIL</h1>
      <hr>
      <h2>{{ article.title }}</h2>
      <p>{{ article.content}}</p>
      <p>작성일: {{ article.created_at }}</p>
      <p>수정일: {{ article.updated_at }}</p>
      <hr>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <a href="{% url 'articles:edit' article.pk %}" class="text-decoration-none btn btn-secondary py-0">
        EDIT
        </a>
        <button class='btn btn-secondary py-0'>DEL</button>
        <a href="{% url 'articles:index' %}" class="text-decoration-none btn btn-secondary py-0">BACK</a>
      </form>
    {% endblock content %}
    ```

### 3. UPDATE

- 2개의 view 필요

  - **edit (views.py)** : 데이터를 수정할 view

    ```python
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            'article': article
        }
        return render(request, 'articles/edit.html', context)
    ```

    **edit (edit.html)**

    ```django
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>NEW</h1>
      <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        </div>
        <label>TITLE:
          <input type="text" name="title" value="{{ article.title }}">
        </label>
        <br>
        <label>CONTENT:<br>
          <textarea name="content"cols="29" rows="10">{{ article.content }}</textarea>
        </label>
        <br>
        <button class="btn btn-secondary py-0">EDIT</button>
        <a href="{% url 'articles:detail' article.pk %}" class="text-decoration-none btn btn-secondary py-0">
        BACK
        </a>
      </form>
    {% endblock content %}
    ```

  - **update (views.py)** : 수정된 데이터를 저장할 view

    ```python
    def update(request, pk):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.get(pk=pk)
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    ```

### 4. DELETE

- POST 메서드로만 제거되도록 처리 필요

- **form tag** 및 **if 문** 사용

  - **delete (views.py)**

    ```python
    def delete(request, pk):
        if request.method == 'POST':
            article = Article.objects.get(pk=pk)
            article.delete()
            return redirect('articles:index')
        else:
            return redirect('articles:detail', pk)
    ```

### 5. 추가

- **redirect( ) 함수**

  - 이미 작성했던 함수를 중복해서 사용하지 않고 해당 함수를 재요청하는 함수

  - view가 자신에게 재요청 => 기존 주소로 변환되어 반환

    ※ render( ) 함수로 요청 시 주소가 해당 view 주소로 변경되어 반환

    ```python
    from django.shortcuts import render, redirect
    
    def view_name(request):
    	return redirect('app_name:view_name')
    ```

- **"GET" 메서드를 이용한 요청**

  - 브라우저 URL을 통한 요청
  - \<a> tag를 통한 요청
  - redirect( ) 함수를 통한 요청

- **Variable Routing 을 이용한 CRUD**

  **① 경로 및 변수 이용**

  ```django
  '/app_name/path_name/{{variable.pk}}'
  ```

  **② {% url %} 태그 이용**

  - 여러 변수 전달 시 공백으로 구분하여 순서대로 입력

  ```django
  {% url 'app_name:path_name' variable.pk %}
  ```

- **관리자 계정 생성 (superuser)**

  - 계정 생성 명령어 (ID, PASSWORD, E-MAIL 등록)

    ```
    $ python manage.py createsuperuser
    ```

  - **admin.py**

    \- 모델 import

    \- 모델 관리자 class 생성 (선택)

    \- 모델에서 \__str__ 메직 메서드로 관리자 페이지 출력명 설정 가능

    ```python
    from django.contrib import admin
    from .models import Article
    
    # 모델 관리자 class를 통해 보다 상세한 관리자 페이지 설정 가능
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title')
    
    admin.site.register(Article, ArticleAdmin)
    ```

    

