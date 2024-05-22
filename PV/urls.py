from django.urls import path
from PV.views import index, sobre, cadastro, logado, consulta, atendimento
from Usuarios.views import cadastro2

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logado/', logado, name='logado'),
    path('consulta/', consulta, name='consulta'),
    path('atendimento/<int:atendimento_id>', atendimento, name='atendimento'),
    path('cadastro2/', cadastro2, name='cadastro2'),
]
