from django.urls import path
from PV.views import index, sobre, consulta, atendimento
from Usuarios.views import cadastro

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
    path('consulta/', consulta, name='consulta'),
    path('atendimento/<int:atendimento_id>', atendimento, name='atendimento'),
]
