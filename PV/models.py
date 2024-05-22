from django.db import models

class Atendimento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    descricao = models.TextField(null=False, blank=False, default='')
    disponivel = models.BooleanField(default=False)    
        
def __str__(self):
    return self.nome

