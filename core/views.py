from django.shortcuts import render
from pessoas.models import Pessoa, Voto

def index(request):
    versao = '0.1'
    return render(request,'index.html',{'versao':versao})

def votacao(request):
    return render(request,'votacao.html')

def obrigado(request):
    return render(request,'obrigado.html')

def teste(request):
    return render(request,'teste.html')