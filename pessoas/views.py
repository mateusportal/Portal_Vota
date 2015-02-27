# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa, Voto

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
        pessoas = Pessoa.objects.filter(ativo='SIM')
        return render(request,'votacao.html',{'pessoas':pessoas})
    else:
        request.session.flush()
        HttpResponseRedirect('/')   

 





