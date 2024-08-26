from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('Passei pelo blog')
    contexto = {
        'title' : 'Blog | By Elias'
    }
    return render(
        request,
        'blog/index.html',
        contexto
    )

def artigo(request):
    print('Passei pelo artigo')
    contexto = {
        'title' : 'Artigo | By Elias'
    }
    return render(
        request,
        'blog/artigo.html',
        contexto,
    )

def doc(request):
    print('Passei pelo doc')

