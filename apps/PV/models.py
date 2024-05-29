from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Atendimento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    descricao = models.TextField(null=False, blank=False, default='')
    disponivel = models.BooleanField(default=False)    
        
class Consultas(models.Model):
    
    OPCOES_DOUTOR = [
        ("ENZO", "Enzo"),
        ("FABIO", "Fabio"),
        ("NG", "Ng"),
        ("QUALQUER UM", "Qualquer Um")
    ]
    
    OPCOES_CONSULTA = [
        ("CATARATA", "Catarata"),
        ("CERATOCONE", "Ceratocone"),
        ("CIRURGIA REFRATIVA", "Cirurgia Refrativa"),
        ("CORNEA E CONJUNTIVA", "Cornea e Conjuntiva"),
        ("GLAUCOMA", "Glaucoma"),
        ("LENTES DE CONTATO", "Lentes de Contato"),
        ("LENTES INTRAOCULAR PREMIUM", "Lente Intraocular Premium"),
        ("OFTALMOLOGIA GERAL", "Oftalmologia Geral"),
        ("OFTALMOPEDIATRIA", "Oftalmopediatria"),
        ("PLASTICA OCULAR", "Plastica Ocular"),
    ]
    
    doutor = models.CharField(max_length=100, choices=OPCOES_DOUTOR, default='QUALQUER UM')
    consulta = models.CharField(max_length=100, choices=OPCOES_CONSULTA, default='')
    descricao = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    data = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
