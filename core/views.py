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
    winners = []
    for dt in datas:
        voto = Voto.objects.filter(data_cadastro__month=dt.month, data_cadastro__year=dt.year)\
        .values('destinatario__pk', 'data_cadastro', 'destinatario__nome', 'destinatario__foto')\
        .annotate(dcount=Count('destinatario__pk')).order_by('-dcount')[:1]

        print Voto.objects.filter(data_cadastro__month=dt.month, data_cadastro__year=dt.year)\
        .values('destinatario__pk', 'data_cadastro', 'destinatario__nome', 'destinatario__foto')\
        .annotate(dcount=Count('destinatario__pk')).order_by('-dcount')[:1]

        winners.append(voto[0])

    print list(winners)

    return render(request,'vencedores.html',{'winners':winners})

def premios(request):
    return render(request,'premios.html')

