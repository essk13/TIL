from django.shortcuts import render
import random

def index(request):
    title = 'title'
    return render(request, 'index.html', {'name': 'EK'})


def greeting(request):
    foods = ['Apple', 'Banana', 'Peach']
    info = {
        'name': 'EK'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)


def dinner(request):
    foods = ['족발', '햄버거', '피자', '치킨']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request.GET.get('title'))
    title = request.GET.get('title')
    
    context = {
        'title': title
    }
    return render(request, 'catch.html',context)


def read(request, user_id, article_number):
    # print(user_id)
    # print(article_number)

    context = {
        'user': user_id,
        'article': article_number,
    }
    return render(request, 'read.html', context)