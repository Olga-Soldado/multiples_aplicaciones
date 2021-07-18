from django.urls import path
from . import views



urlpatterns = [
    path('', views.root),
    path('blogs', views.indice),
    path('blogs/new', views.nuevo),
    path('blogs/create', views.crear),
    path('blogs/<int:num>', views.show),
    path('blogs/<int:num>/edit', views.editar),
    path('blogs/<int:num>/delete', views.destruir),   
]