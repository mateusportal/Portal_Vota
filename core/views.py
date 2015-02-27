# coding: utf-8
from django.shortcuts import render
from pessoas.models import Pessoa, Voto

def index(request):
    versao = '0.1'
    request.session.flush()
    return render(request,'index.html',{'versao':versao})

def obrigado(request):
    request.session.flush()
    return render(request,'obrigado.html')

def vencedores(request):
    request.session.flush()
    return render(request,'vencedores.html')

