from django.urls import path
from apps.Usuarios.views import cadastro, login,  logout
from apps.PV.views import index

urlpatterns = [
     path('cadastro/', cadastro, name='cadastro'),
     path('login/', login, name='login'),
     path('index/', index, name='index'),
     path('logout', logout, name='logout')
]
