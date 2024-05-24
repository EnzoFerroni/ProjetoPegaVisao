from django.shortcuts import render, get_object_or_404
from PV.models import Atendimento
from Usuarios.forms import LoginForms

def index(request):
    form = LoginForms()
    atendimento = Atendimento.objects.filter(disponivel=True)
    return render(request, 'clinica/index.html', {"cards": atendimento, 'form':form})

def sobre(request):
    form = LoginForms()
    return render(request, 'clinica/sobre.html', {'form':form})

def consulta(request):
    form = LoginForms()
    return render(request, 'clinica/consulta.html', {'form':form})

def atendimento(request, atendimento_id):
    form = LoginForms()
    atendimento = get_object_or_404(Atendimento, pk=atendimento_id)
    return render(request, 'clinica/atendimento.html', {"atendimento": atendimento, 'form':form})