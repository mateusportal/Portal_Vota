# coding: utf-8
from django.shortcuts import render
from pessoas.models import Pessoa, Voto

def index(request):
    request.session.flush()
    return render(request,'index.html')

def obrigado(request):
    request.session.flush()
    return render(request,'obrigado.html')

def vencedores(request):
    #request.session.flush()
    #votos = Voto()

    #print votos.campeoes()

    return render(request,'vencedores.html')

