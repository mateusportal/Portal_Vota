# coding: utf-8
from django.shortcuts import render
from pessoas.models import Pessoa, Voto
from django.db.models import Count

def index(request):
    request.session.flush()
    return render(request,'index.html')

def obrigado(request):
    request.session.flush()
    return render(request,'obrigado.html')

def vencedores(request):
    request.session.flush()

    pessoas = Pessoa.objects.filter(
    data_cadastro__year=2015, 
    data_cadastro__month=2).annotate(qtde=Count('votos')).values('destinatario', 'qtde').order_by('-qtde')

    return render(request,'vencedores.html')

