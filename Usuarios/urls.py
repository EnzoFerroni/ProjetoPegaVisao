from django.urls import path
from Usuarios.views import cadastro, login,  logout
from PV.views import index

urlpatterns = [
     path('cadastro/', cadastro, name='cadastro'),
     path('login/', login, name='login'),
     path('index/', index, name='index'),
     path('logout', logout, name='logout')
]
