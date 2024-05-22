from django import forms

#LOGIN

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    senha_confirmacao=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
#CADASTRO 

# class CadastroForms(forms.Form):
#     nome_cadastro=forms.CharField(
#         label="Nome de Cadastro",
#         required=True,
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email_cadastro=forms.EmailField(
#         label="Email de Cadastro",
#         required=True,
#         max_length=100,
#         widget=forms.EmailField(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     senha_cadastro=forms.CharField(
#         label="Senha",
#         required=True,
#         max_length=100,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     senha_confirmacao=forms.CharField(
#         label="Senha",
#         required=True,
#         max_length=100,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )