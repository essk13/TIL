from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('delete/', views.delete , name='delete'),
    path('update/', views.chg_user , name='chg_user'),
    path('password/', views.chg_pw , name='chg_pw'),
]