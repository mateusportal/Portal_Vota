# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from pessoas.models import Pessoa, Voto
from datetime import date

def valida_login(request):
    request.session.flush()
    if request.method == 'POST':
        email = request.POST.get('email', '').upper()
        cpf = request.POST.get('cpf', '').upper()

        if (len(email.strip()) > 0) and (len(cpf.strip()) > 0):
            try:
                pessoa = Pessoa.objects.get(email__iexact=email, cpf=cpf, ativo='SIM')

                if pessoa:
                    request.session['email'] = email
                    request.session['cpf'] = cpf
                    request.session['foto'] = pessoa.foto
                    request.session['nome'] = pessoa.nome
                    request.session['area'] = pessoa.area
                    request.session['id'] = pessoa.pk
                    return HttpResponseRedirect('/votacao/')
                else:
                    return render(request,'index.html',{'msg':'Não foi encontrado o usuário no sistema. Tente novamente.','email':email,'cpf':cpf})  
            except:
                return render(request,'index.html',{'msg':'Erro ao consultar colaborador! Revise as informações e tente novamente.','email':email,'cpf':cpf})  
    
    return HttpResponseRedirect('/')   

def votacao(request):
    if request.session.get('id', False) and request.session.get('id') > 0:
        pessoas = Pessoa.objects.filter(ativo='SIM').exclude(pk=request.session.get('id')).order_by('nome')
        return render(request,'votacao.html',{'pessoas':pessoas})
    else:
        request.session.flush()
        return HttpResponseRedirect('/')     

def votar(request, codigo):
    validacao = True

    if not codigo:
        validacao = False
    elif not codigo.isdigit():
        validacao = False
    elif codigo <= 0:
        validacao = False

    if validacao:
        data = date.today()

        try:
            votos = Voto.objects.get(remetente_id=request.session['id'], data_cadastro__month=data.month) 
            votos.destinatario_id = codigo
            votos.save()
        except:
            votos = Voto(remetente_id=request.session['id'], destinatario_id=codigo)
            votos.save()

        request.session.flush()
        return HttpResponseRedirect('/obrigado/')
    else:
        request.session.flush()
        return HttpResponseRedirect('/')