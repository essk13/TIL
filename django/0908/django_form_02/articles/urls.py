from collections import namedtuple
from typing import Mapping
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]