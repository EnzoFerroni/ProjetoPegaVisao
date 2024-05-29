from django.contrib import admin
from apps.PV.models import Atendimento, Consultas

class ListandoAtendimentos(admin.ModelAdmin):
    list_display=("id", "nome", "disponivel")
    list_display_links=("id", "nome")
    search_fields = ("nome",)
    list_editable = ("disponivel",)

admin.site.register(Atendimento, ListandoAtendimentos)

class ListandoConsultas(admin.ModelAdmin):
    list_display = ("id", "usuario", "doutor", "consulta" )
    list_display_links=("id", "usuario")
    search_fields = ("usuario",)

admin.site.register(Consultas, ListandoConsultas)
