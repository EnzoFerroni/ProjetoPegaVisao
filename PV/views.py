from django.shortcuts import render

def index(request):
    return render(request, 'clinica/index.html')

def sobre(request):
    return render(request, 'clinica/sobre.html')

def cadastro(request):
    return render(request, 'clinica/cadastro.html')