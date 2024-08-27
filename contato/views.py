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

    return exibe(request)
    


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

def editar(request, id):
        pessoa = Pessoa.objects.get(id_pessoa=id)
        return render(
            request,
            'contato/editar.html',
            {"pessoa": pessoa}
        )


def atualizar(request, id):
        pessoa = Pessoa.objects.get(id_pessoa=id)
        pessoa.nome = request.POST.get('nome')
        pessoa.idade = request.POST.get('idade')
        pessoa.email = request.POST.get('email')
        pessoa.save()

        return exibe(request)

def apagar(request, id):
        pessoa = Pessoa.objects.get(id_pessoa=id)
        pessoa.delete()
        return exibe(request)
