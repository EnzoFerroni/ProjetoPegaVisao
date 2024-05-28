from django.shortcuts import render, get_object_or_404, redirect
from apps.PV.models import Atendimento
from apps.Usuarios.forms import LoginForms
from django.contrib import messages
from apps.PV.forms import ConsultaForms

def index(request):
    form = LoginForms()
    atendimento = Atendimento.objects.filter(disponivel=True)
    return render(request, 'clinica/index.html', {"cards": atendimento, 'form':form})

def sobre(request):
    form = LoginForms()
    return render(request, 'clinica/sobre.html', {'form':form})


def atendimento(request, atendimento_id):
    form = LoginForms()
    atendimento = get_object_or_404(Atendimento, pk=atendimento_id)
    return render(request, 'clinica/atendimento.html', {"atendimento": atendimento, 'form':form})

def nova_consulta(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login ou realize o cadastro antes de marcar uma consulta!")
        return redirect ('index')
    form = ConsultaForms()
    return render(request, 'clinica/consulta.html', {'form':form})

def editar_consulta(request):
    pass

def deletar_consulta(request):
    pass