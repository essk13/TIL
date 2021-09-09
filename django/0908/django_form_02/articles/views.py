from articles.forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    '''
    모든 데이터 확인
    '''
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    '''
    새로운 데이터 등록
    '''
    # POST 메서드 사용 시 DB에 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    # GET 메서드 사용 시 입력 폼을 생성하여 전달
    else:
        form = ArticleForm()
    # 유효성 검사 실패시 오류 메시지 전달
    context = {
        'form': form,
        'btn_name': 'WRITE'
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    '''
    데이터 상세정보 열람
    '''
    # 열람할 데이터 선택
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    # 수정할 데이터 호출
    article = get_object_or_404(Article, pk=pk)
    # POST 메서드 사용 시 데이터 수정
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', pk)
    # 수정 페이지를 위해 form 사용
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
        'btn_name': 'UPDATE',
    }
    return render(request, 'articles/form.html', context)


def delete(request, pk):
    '''
    데이터 삭제
    '''
    if request.method == 'POST':
        # 삭제할 데이터 선택
        article = get_object_or_404(Article, pk=pk)
        article.delete()    # 데이터 삭제 메서드
        return redirect('articles:index')
