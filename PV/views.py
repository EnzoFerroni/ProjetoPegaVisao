from django.shortcuts import render
from PV.models import Atendimentos

def index(request):
    atendimento = Atendimentos.objects.all()
    return render(request, 'clinica/index.html', {"cards": atendimento})

def sobre(request):
    return render(request, 'clinica/sobre.html')

def cadastro(request):
    return render(request, 'clinica/cadastro.html')

def logado(request):
    return render(request, 'clinica/logado.html')

def consulta(request):
    return render(request, 'clinica/consulta.html')