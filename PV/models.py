from django.db import models

class Atendimento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False, default='F')    
    
#class Especialidades(models.Model):
    
def __str__(self):
    return "Atendimento [nome={self.nome}]"

