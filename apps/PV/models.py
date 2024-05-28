from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Atendimento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    descricao = models.TextField(null=False, blank=False, default='')
    disponivel = models.BooleanField(default=False)    
        
class Consulta(models.Model):
    
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
    
    nome = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    doutor = models.CharField(max_length=100, choices=OPCOES_DOUTOR, default="QUALQUER UM")
    consulta = models.CharField(max_length=100, choices=OPCOES_CONSULTA)
    data_consulta = models.DateTimeField(default=datetime.now, blank=False)
    descricao = models.TextField(null=True, blank=True)