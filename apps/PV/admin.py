from django.contrib import admin
from apps.PV.models import Atendimento

class ListandoAtendimentos(admin.ModelAdmin):
    list_display=("id", "nome", "disponivel")
    list_display_links=("id", "nome")
    search_fields = ("nome",)
    list_editable = ("disponivel",)

admin.site.register(Atendimento, ListandoAtendimentos)