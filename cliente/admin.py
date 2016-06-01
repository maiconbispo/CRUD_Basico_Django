from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	date_hierarchy = 'data_nascimento'
	list_display = ('id', 'nome', 'data_nascimento','email',)
	list_filter = ('nome', 'data_nascimento', 'email')

admin.site.register(Cliente, ClienteAdmin)
