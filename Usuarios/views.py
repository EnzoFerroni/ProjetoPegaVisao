from django.shortcuts import render, redirect
from Usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid(): 
            if form["senha_cadastro"].value() != form["senha_cadastro_confirmacao"].value():
                return redirect('cadastro')
            
            nome=form["nome_cadastro"].value()
            email=form["email_cadastro"].value()
            senha=form["senha_cadastro"].value()
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('index')
    return render(request, 'usuarios/cadastro.html', {'form':form})

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form':form})