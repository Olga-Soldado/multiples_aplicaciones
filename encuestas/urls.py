from django.urls import path
from . import views



urlpatterns = [
    path('', views.root),
    path('encuestas', views.indice),
    path('encuestas/new', views.nuevo), 
]