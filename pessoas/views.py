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
                    request.session['id'] = pessoa.pk
                    return HttpResponseRedirect('/votacao/')
                else:
                    return render(request,'index.html',{'msg':'Não foi encontrado o usuário no sistema. Tente novamente.','email':email,'cpf':cpf})  
            except:
                return render(request,'index.html',{'msg':'Erro ao consultar colaborador! Revise as informações e tente novamente.','email':email,'cpf':cpf})  
    
    return HttpResponseRedirect('/')   

def votacao(request):
    if request.session.get('id', False):
        pessoas = Pessoa.objects.filter(ativo='SIM').exclude(pk=request.session.get('id')).order_by('nome')
        return render(request,'votacao.html',{'pessoas':pessoas})
    else:
        request.session.flush()
        HttpResponseRedirect('/')     

def votar(request, codigo):
    data = date.today()


    try:
        votos = Voto.objects.get(remetente=codigo,data_cadastro__month = data.month)
        voto.destinatario = codigo
        votos.save()
    except:
        votos = Voto(destinatario=codigo, remetente=request.session.get['id'])
        votos.save()

    request.session.flush()
    return HttpResponseRedirect('/obrigado/')

       
    
>>>>>>> ef84bbb1bf17f72456ae6940205c4297e53fe8e8
 





