from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    contexto = {
        'title' : 'Home | By Elias'
    }
    return render(
        request,
        'home/index.html',
        contexto
    )

