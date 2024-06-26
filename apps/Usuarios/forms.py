from typing import Any
from django import forms

#FORMULARIO DE LOGIN

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu nome"
            }
        )
    )

    senha_login=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"

            }           
        )
    )

#FORMULARIO DE CADASTRO

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu nome"
            }
        )
    )
    
    email_cadastro=forms.EmailField(
        label="Email de Cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )
    
    senha_cadastro=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"

            }           
        )
    )
    
    senha_cadastro_confirmacao=forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"

            }           
        )
    )
            
    # def clean_senha_cadastro_confirmacao(self):
    #     senha_cadastro = self.cleaned_data.get("senha_cadastro")
    #     senha_cadastro_confirmacao = self.cleaned_data.get("senha_cadastro_confirmacao")
        
    #     if senha_cadastro and senha_cadastro_confirmacao:
    #         if senha_cadastro != senha_cadastro_confirmacao:
    #             raise forms.ValidationError("Senhas não são iguais")
    #         else:
    #             return senha_cadastro_confirmacao