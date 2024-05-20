from django.urls import path
from PV.views import index, sobre, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cadastro/', cadastro, name='cadastro'),
]
