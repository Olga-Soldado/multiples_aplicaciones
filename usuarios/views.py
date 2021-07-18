from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def indice(request):
    return redirect("/users")
def user(request):
    return HttpResponse("marcador de posición para luego mostrar toda la lista de usuarios")
def register(request):
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")
def login(request):
    return HttpResponse("marcador de posición para que los usuarios inicien sesión")
def nuevo(request):
    return redirect("/register")
def root(request):
    return redirect("/blogs/blogs")