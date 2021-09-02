from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('delete/<pk>/', views.delete, name='delete'),
    path('update/<pk>/', views.update, name='update'),
    path('<pk>/edit/', views.edit, name='edit'),
    path('detail/<pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index')
]
