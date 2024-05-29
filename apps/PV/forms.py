from django import forms
from apps.PV.models import Consultas
from django.forms.widgets import DateTimeInput

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultas
        exclude = ['status', 'usuario']
        labels = {
            'descricao':'Descrição'
        }
    
        widgets = {
            'doutor': forms.Select(attrs={'class':'form-control'}),
            'consulta': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(
                attrs={
                    'placeholder': 'Deseja compartilhar algo a mais para a consulta? (Caso não deseje deixe em branco)',
                    'class':'form-control'
                    }
            ),
            'data': forms.DateTimeInput(
                format = "%d/%m/%y %H:%M",
                attrs={
                    'type':'datetime-local',
                    'class':'form-control'
                }
            ),
        }