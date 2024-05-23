from django.urls import path
from Usuarios.views import cadastro, login
from PV.views import index

urlpatterns = [
     path('cadastro/', cadastro, name='cadastro'),
     path('login/', login, name='login'),
     path('index/', index, name='index'),
]
