from django.shortcuts import render
from pessoas.models import Pessoa, Voto

def index(request):
    versao = '0.1'
    return render(request,'index.html',{'versao':versao})

def login(request):

    email = request.POST.get('email','SEM EMAIL')

    print email
    #pessoa = Pessoa.objects.get(email=, cpf=)
    return render(request,'votacao.html',{'nome':email})
