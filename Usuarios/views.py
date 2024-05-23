from django.shortcuts import render, redirect
from Usuarios.forms import LoginForms
from django.contrib.auth.models import User

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form':form})