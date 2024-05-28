from django import forms
from apps.PV.models import Consulta

class ConsultaForms(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude= ['nome',]
        widgets={
            'consulta': forms.Select(attrs={'class':'form-control'}),
            'doutor': forms.Select(attrs={'class':'form-control'}),
            'data': forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    'type': 'date',
                    'class':'form-control'
                }
            ),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
        }