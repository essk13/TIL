from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/', views.post_list_create),
    path('posts/<post_pk>/', views.post_detail_update_delete),
]