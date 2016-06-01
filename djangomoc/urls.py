from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  'cliente.views.home', name='cliente_home'),
    url(r'^cliente/$', 'cliente.views.cliente', name='cliente_principal'),
    url(r'^cliente_update/(?P<pk>\d+)$', 'cliente.views.update', name='cliente_update'),
    url(r'^cliente_novo/$', 'cliente.views.create', name='cliente_create'),
    url(r'^cliente_delete/(?P<pk>\d+)$', 'cliente.views.delete', name='cliente_delete'),
]
