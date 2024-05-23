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

    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
           
        )
    )
   