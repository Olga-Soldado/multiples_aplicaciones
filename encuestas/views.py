from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def root(request):
    return redirect("/encuestas")
def indice(request):
    return HttpResponse("marcador de posición para mostrar todas las encuestas creadas")
def nuevo(request):
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")