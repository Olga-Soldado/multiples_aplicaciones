from django.urls import path
from . import views



urlpatterns = [
    path('', views.root),
    path('users', views.user),
    path('users/new', views.nuevo),
    path('login', views.login),
    path('register',views.register)
    
]