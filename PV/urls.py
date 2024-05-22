from django.urls import path
from PV.views import index, sobre, cadastro, logado, consulta

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logado/', logado, name='logado'),
    path('consulta/', consulta, name='consulta'),


]
