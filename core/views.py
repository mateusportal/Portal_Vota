# coding: utf-8
from django.shortcuts import render
from pessoas.models import Pessoa, Voto
from django.db.models import Count
import itertools

def index(request):
    request.session.flush()
    return render(request,'index.html')

def obrigado(request):
    request.session.flush()
    return render(request,'obrigado.html')

def vencedores(request):
    from django.db import connection
    from django.db.models import Sum, Count
    request.session.flush()

    datas = Voto.objects.all().datetimes('data_cadastro','month',order='DESC')
    listaVotos = {}
    for dt in datas:
        votos = Voto.objects.filter(data_cadastro__month=dt.month, data_cadastro__year=dt.year).values('destinatario_id').annotate(dcount=Count('id')).order_by('-dcount')[:1]

        listaVotos = itertools.chain(listaVotos,votos.destinatario_id)

    print list(listaVotos)

    #tenho que retornar algo assim para o template para mostrar e listar os ganhadores por ano e mes, e claro, a foto com o nome
    listagem = [{'ano': 2015, 'mes': 3, 'nome': 'edson', 'foto': 'leo.jpg'}, {'ano': 2014, 'mes': 2, 'nome': 'Leo', 'foto': 'claudio.jpg'}]

    return render(request,'vencedores.html',{'listagem':listagem})

