from django.shortcuts import render, get_object_or_404, redirect
from apps.PV.models import Atendimento
from apps.Usuarios.forms import LoginForms
from django.contrib import messages
from apps.PV.forms import ConsultaForm
from django.contrib.auth.decorators import login_required


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

@login_required
def nova_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)  # Não salvar ainda
            consulta.usuario = request.user  # Associar ao usuário logado
            consulta.save()
            return redirect('index')  # Redirecionar para onde desejar
    else:
        form = ConsultaForm()
    return render(request, 'clinica/consulta.html', {'form': form})
def editar_consulta(request):
    pass

def deletar_consulta(request):
    pass

def marcadas(request):
    
    return render(request, 'clinica/marcadas.html', {"marcadas": marcadas})
