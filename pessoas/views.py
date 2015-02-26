# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa, Voto

def valida_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        cpf = request.POST.get('cpf', '')
        request.session.flush()

        if (len(email.strip()) > 0) and (len(cpf.strip()) > 0):
            try:
                pessoa = Pessoa.objects.get(email=email, cpf=cpf, ativo='SIM')

                if pessoa:
                    request.session['email'] = email
                    request.session['cpf'] = cpf
                    HttpResponseRedirect('/votacao/')
                else:
                    render(request,'index.html',{'msg':'Não foi encontrado o usuário no sistema. Tente novamente.','email':email,'cpf':cpf})  
                    HttpResponseRedirect('/')
            except:
                render(request,'index.html',{'msg':'Erro ao consultar colaborador! Revise as informações e tente novamente.','email':email,'cpf':cpf})  



def votacao(request):
    if request.session.get('email', False):
        #Abrir página com a listagem dos usuários para a votacao.
        pessoas = Pessoa.objectes.filter(ativo='SIM').order('nome')

        HttpResponseRedirect('')
    else:
        request.session.flush()
        HttpResponseRedirect('/')   
 





