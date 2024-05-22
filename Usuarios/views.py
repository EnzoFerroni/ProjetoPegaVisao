from django.shortcuts import render, redirect
from Usuarios.forms import LoginForms
from django.contrib.auth.models import User

def cadastro2(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            if form["senha"].value() != form["senha_confirmacao"].value():
                return redirect('cadastro2')
        
            nome=form["nome_login"].value()
            email=form["email"].value()
            senha=form["senha"].value()
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro2')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('index')
            
    return render(request, 'usuarios/cadastro2.html', {"form": form})