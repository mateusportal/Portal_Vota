from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa, Voto

def valida_login(request):
	if request.method == 'POST':
		email = request.POST.get('email', '')
		cpf = request.POST.get('cpf', '')

		if (len(email.strip()) > 0) and (len(cpf.strip()) > 0):
			try:
				pessoa = Pessoa.objects.get(email=email, cpf=cpf)
			except:
				render(request,'index.html',{'msg':'Erro ao consultar colaborador!'})	





