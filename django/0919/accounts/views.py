from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import ( UserCreationForm,
                                        AuthenticationForm,
                                        PasswordChangeForm,
                                       )
from .forms import CutsomUserChageForm, CustomUserCreationForm
from django.views.decorators.http import ( require_POST,
                                           require_http_methods,
                                          )
from django.contrib.auth import ( login as auth_login,
                                  logout as auth_logout,
                                  update_session_auth_hash,
                                 )

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('new') or 'articles:index')
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


@login_required
@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def chg_user(request):
    if  request.method == 'POST':
        form = CutsomUserChageForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CutsomUserChageForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/chg_user.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def chg_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/chg_pw.html', context)
