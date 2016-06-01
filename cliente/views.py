from django.shortcuts import render, redirect
from django.http import HttpResponse
from cliente.models import Cliente
from cliente.forms import ClienteForm

def home(request):
	return HttpResponse("Hello World")

def cliente(request):
	data = {} #Variavel criada
	data['lista_clientes'] = Cliente.objects.all() #SELECT DO BANCO
	data['djangomoc'] = 'DjangoMOC - Melhor curso de Django' #Variavel declarada
	return render(request, 'clientes.html', data) #Variavel enviada pro template

def update(request, pk):
	cliente = Cliente.objects.get(pk=pk) # NOME DA CLASSE.objects.get(PARAMETRO WHERE)
	form = ClienteForm(request.POST or None, instance=cliente)

	if form.is_valid():
		form.save()
		return redirect('cliente_principal')

	return render(request, 'cliente_detalhe.html',{'object':cliente, 'form':form})

def create(request):
	form = ClienteForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cliente_principal')
	return render(request, 'cliente_novo.html', {'form':form} )

def delete(request, pk):
	cliente = Cliente.objects.get(pk=pk)

	if request.method == 'POST':
		cliente.delete()
		return redirect('cliente_principal')
	return render(request, 'cliente_delete_confirm.html', {'object':cliente})
