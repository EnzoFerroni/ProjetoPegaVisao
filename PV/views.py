from django.shortcuts import render, get_object_or_404
from PV.models import Atendimento

def index(request):
    atendimento = Atendimento.objects.all()
    return render(request, 'clinica/index.html', {"cards": atendimento})

def sobre(request):
    return render(request, 'clinica/sobre.html')

def cadastro(request):
    return render(request, 'clinica/cadastro.html')

def logado(request):
    return render(request, 'clinica/logado.html')

def consulta(request):
    return render(request, 'clinica/consulta.html')

def atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, pk=atendimento_id)
    return render(request, 'clinica/atendimento.html', {"atendimento": atendimento})