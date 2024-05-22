from django.urls import path
from Usuarios.views import cadastro2
from PV.views import index

urlpatterns = [
     path('cadastro2/', cadastro2, name='cadastro2'),
     path('index/', index, name='index'),

]
