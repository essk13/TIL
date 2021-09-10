from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'articles': articles,
        'page_obj': page_obj,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.add_message(request, messages.INFO, 'CONTENT CREATED')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/form.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'CONTENT UPDATED')
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.error(request, 'CONTENT DELETE')
    return redirect('articles:index')