from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import ( login as auth_login,
                                  logout as auth_logout,
                                 )
from django.contrib.auth.forms import ( UserCreationForm,
                                        AuthenticationForm,
                                        PasswordChangeForm,
                                       )
from .forms import CustomUCF

# Create your views here.
@require_http_methods(['GET', "POST"])
def signup(request):
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


@require_http_methods(['GET', "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', "POST"])
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


@login_required
@require_http_methods(['GET', "POST"])
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