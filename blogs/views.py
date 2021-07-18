from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def root(request):
    return redirect("/blogs/blogs")
def indice(request):
    return HttpResponse("marcador de posición para luego mostrar una lista de todos los blogs")
def nuevo(request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")
def crear(request):
    return redirect('/blogs')
def show(request, num):
    return HttpResponse(f"marcador de posición para mostrar el número de blog: {num}")
def editar(request, num):
    return HttpResponse(f"marcador de posición para editar el blog {num}")
def destruir(request, num):
    return redirect("/blogs")