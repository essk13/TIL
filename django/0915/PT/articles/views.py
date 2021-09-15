import articles
from django.db.models.fields import AutoField
from django.forms.models import ALL_FIELDS
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArticleFrom
from .models import Article
from django.views.decorators.http import require_POST, require_http_methods ,require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleFrom(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleFrom()
    context = {
        'form': form,
        'btn_name': 'CREATE'
    }
    return render(request, 'articles/form.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleFrom(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleFrom(instance=article)
    context = {
        'form': form,
        'btn_name': 'UPDATE'
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')