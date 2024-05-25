from django.shortcuts import render, redirect
from apps.Usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid(): 
            if form["senha_cadastro"].value() != form["senha_cadastro_confirmacao"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')
            
            nome=form["nome_cadastro"].value()
            email=form["email_cadastro"].value()
            senha=form["senha_cadastro"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Nome de cadastro já existe")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f"Cadastro de {nome} efetuado com sucesso!")
            return redirect('index')
    return render(request, 'usuarios/cadastro.html', {'form':form})

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha_login'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"Usuario logado com sucesso! Seja bem-vindo(a) {nome}!")
            return redirect('index')

        else:
            messages.error(request, "Login inválido, tente novamente ou realize o cadastro primeiro!")
            return redirect('index')
    return render(request, 'clinica/index')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('index')