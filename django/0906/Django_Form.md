# Django_Form

## 1. Django Form Class

- HTML `<form>`, `<input>`을 사용하면 유효성 검증 및 올바른 작동을 위한 작업이 복잡함

- **Django form**

  - 프로젝트의 주요 **유효성 검사 도구** 중 하나 / 공격 및 데이터 손상에 대한 방어 수단

  - HTML `<form>`에 비해 **단순화 및 자동화**가 가능하고 **안정성**이 높음

    **① 랜더링을 위한 데이터 준비 및 재구성**

    **② 데이터에 대한 HTML forms 생성**

    **③ 전달 받은 데이터 수신 및 처리**

- **Form Class**

  - field, field배치, 디스플레이 widget, label, 초기값 상태 결정
  - 유효하지 않는 field에 관련된 **에러 메시지 결정 (자동생성)**
  - **과중한 작업(유효성 검사, 검증결과 출력 등) 및 중복 제거**

  - **Form 선언 (forms.py)**

    **\- Model 선언과 유사 / 같은 Field 타입 사용 (모든 Field가 존재하지는 않음)**

    \- forms 라이브러리 Form 클래스 상속

    ```python
    from django import forms
    
    class Model_nameForm(forms.Form):
        attribute1 = form.CharField(max_length=10)
        attribute2 = form.CharField()
    ```

  - **Form 사용**

    - **View**

      ```python
      def path_name(request):
          form = App_nameForm()
          context = {
              'form': form
          }
          return render(request, 'app_name/path_name.html', context)
      ```

    - **Template**

      **\- .as_p()**

      ​	· `<p>` 각 field `</p>`

      **\- .as_ul()**

      ​	· `<li>` 각 field `</li>`

      **\- .as_table()**

      ​	· `<tr>` 각 field `</tr>`

      ```django
      {% extends 'skeleton.html' %}
      
      {% block content %}
        {{ form.as_p }}
      {% endblock %}
      ```

- Django HTML input 요소 표현 방법

  - **Form fields**
    - input에 대한 **유효성 검사 로직** 처리
    - Template에서 직접 사용
  - **Widgets**
    - 웹 페이지의 HTML input 요소 렌더링
    - GET/POST 딕셔너리의 데이터 추출
    - **form fields에 할당**

- **Widget**

  - input 요소의 단순 렌더링 처리

  - **form field에 할당되어 작성**

    ```python
    from django import forms
    
    class Model_nameForm(forms.Form):
        attribute1 = form.CharField(max_length=10)
        attribute2 = form.CharField(widget=forms.Textarea)
    ```

## 2. Model Form

- model과 **form을 정의함에 있어 중복을 제거하기 위한 Helper**

- 일반 Form Class와 같은 방식으로 view에서 사용 가능

- **ModelForm 선언**

  - ModelForm 클래스 상속

  - 정의한 클래스 내부에 **innerclass로 Meta 클래스 선언**

  - Meta클래스에 기반 **model 및 field 정보 작성**

    ```python
    class Model_nameForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__' 		   # 모든 field
            (exclude = ('attribute',)) # 제거 할 field
    ```

- **Meta Class**

  - Model의 정보를 작성하는 곳
  - **Form에 적용할 model과 field 정보를 정의**
  - Inner Class (Nested Class)
    - 클래스 내에 선언된 다른 클래스
    - 가독성 향상, 유지 관리 지원 및 복잡성 감소
  - Meta 데이터
    - 데이터를 설명하기 위한 데이터

- **`is_valid()` method**

  - **유효성 검사** 실행, 데이터 **유효 여부를 boolean 값으로 반환**

- **`save()` method**

  - form에 바인딩 된 데이터에 대한 데이터베이스 객체를 만들고 저장
  - `instance=` 인자 할당 가능
    - **`instance` 인자 미할당 = CREATE**
    - **`instance` 인자 할당 = UPDATE**
  - form의 유효성이 확인되지 않은 경우 `save()` 호출 시 form.errors를 확인하여 에러 확인 가능

- **Widget 적용**

  - Meta class 내부에 작성

    ```python
    class Model_nameForm(forms.ModelForm):
        class Meta:
            model = Model_name
            fields = '__all__'
            widgets = {
                'attribute': forms.Field_type(attrs = {
                    'class': '',
                    'style1': 'value',
                    'style2': 'value',
                })
            }
    ```

  - **Meta class 외부에 작성** (권장)

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

## 3. 정리

- **Form**

  - 어떤 model에 저장해야하는지 알 수 없음

  - 유효성 검사 후 cleaned_data 딕셔너리 생성

  - **cleaned_data 딕셔너리에서 데이터를 가져온 후  `.save()` 호출 (Model에 저장)**

    ```python
    if form.is_valid():
        attrs1 = form.cleaned_data.get('attribute1')
        attrs2 = form.cleaned_data.get('attribute2')
        model_name = Model_name.objects.create(attribute1=attrs1, attriubte2=attrs2) # .save()사용 가능
    ```

  - **model에 연관되지 않은 데이터를 받을 때 사용**

- **ModelForm**

  - Django가 해당 **model에서** 양식에 필요한 대부분의 **정보를 사전 정의**
  - 어떤 레코드를 작성해야 할 지 알고 있음
  - **`.save()` 바로 호출** 가능

  **※ 사용 상황이 다른 것 / ModelForm이 Form보다 좋다는 개념이 아님 ※**



## 4. Django Form(ModelForm)을 활용한 CRUD

- **CREATE (New + Create / GET, POST)**

  ```python
  @require_http_methods(['GET', 'POST'])
  def create(request):
      # create
      if request.method == 'POST':
          form = Model_nameForm(request.POST)
          # 유효성 검사
          if form.is_valid():
              model_name = form.save()
              return redirect('app_name:detail', model_name.pk)
      # new
      else:
          form = Model_nameForm()
  	# if, else와 같은 레벨에 작성 #
      # 유효성 검사 실패 시 context를 통해 에러 메시지 전달 #
      context = {
          'form': form,
      }
      return render(request, 'app_name/create.html', context)
  ```

- **READ(Detail)**

  ```python
  @require_safe
  def detail(request, pk):
      # model_name = Model_name.objects.get(pk=pk)
      model_name = get_object_or_404(Article, pk=pk)
      context = {
          'model_name': model_name,
      }
      return render(request, 'app_name/detail.html', context)
  ```

- **UPDATE**

  ```python
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      # model_name = Model_name.objects.get(pk=pk)
      model_name = get_object_or_404(Model_name, pk=pk)
      # update
      if request.method == 'POST':
          form = Model_nameForm(request.POST, instance=model_name)
          if form.is_valid():
              form.save()
              return redirect('app_name:detail', model_name.pk)
      # edit
      else:
          form = Model_nameForm(instance=model_name)
  	# if, else와 같은 레벨에 작성 #
      # 유효성 검사 실패 시 context를 통해 에러 메시지 전달 #
      context = {
          'model_name': model_name,
          'form': form,
      }
      return render(request, 'app_name/update.html', context)
  ```

- **DELETE**

  ```python
  # require_POST 데코레이터를 통해 if request.method == 'POST' 조건 대체 #
  @require_POST
  def delete(request, pk):
      # model_name = Model_name.objects.get(pk=pk)
      model_name = get_object_or_404(Model_name, pk=pk)
      model_name.delete()
      return redirect('app_name:index')
  ```

  

