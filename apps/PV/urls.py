from django.urls import path
from apps.PV.views import\
    index, sobre, atendimento, nova_consulta, editar_consulta, deletar_consulta
from apps.Usuarios.views import cadastro

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
    path('atendimento/<int:atendimento_id>', atendimento, name='atendimento'),
    path('nova-consulta/', nova_consulta, name='nova_consulta'),
    path('editar-consulta/', editar_consulta, name='editar_consulta'),
    path('deletar-consulta/', deletar_consulta, name='deletar_consulta'),

]
