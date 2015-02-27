# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa, Voto

def valida_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').upper()
        cpf = request.POST.get('cpf', '').upper()
        request.session.flush()

        if (len(email.strip()) > 0) and (len(cpf.strip()) > 0):
            try:
                pessoa = Pessoa.objects.get(email__iexact=email, cpf=cpf, ativo='SIM')

                if pessoa:
                    request.session['email'] = email
                    request.session['cpf'] = cpf
                    return HttpResponseRedirect('/votacao/')
                else:
                    render(request,'index.html',{'msg':'Não foi encontrado o usuário no sistema. Tente novamente.','email':email,'cpf':cpf})  
                    return HttpResponseRedirect('/')
            except:
                return render(request,'index.html',{'msg':'Erro ao consultar colaborador! Revise as informações e tente novamente.','email':email,'cpf':cpf})  



def votacao(request):
   # if request.session.get('email', False):

    pessoas = Pessoa.objects.filter(ativo='SIM')
    for pessoa in pessoas:
        print pessoa.nome 

    return render(request,'votacao.html',{'pessoas':pessoas})
    #else:
    #    request.session.flush()
    #    HttpResponseRedirect('/')   

def votar(request, codigo):
    
 





