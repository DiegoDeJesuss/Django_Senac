from django.shortcuts import render
#from django.http import HttpResponse

from .models import Pessoa

# Create your views here.
def contato(request):  
    contexto = {
        'title' : 'Contato | By Elias'
    }
    return render(
        request,
        'contato/index.html',
        contexto
    )

def gravar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome  = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()

    return contato(request)


def exibe(request):
    # exibir todas as pessoas

    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }

    return render(
        request,
        'contato/mostrar.html',
         exibe_pessoas,
    )