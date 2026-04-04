from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display        = ('id', 'nome', 'legenda', 'descricao','publicada')
    list_display_links  = ('id', 'nome')
    search_fields       = ('nome', 'legenda', 'descricao')
    list_filter         = ('categoria', 'publicada')
    list_editable       = ('publicada',)
    list_per_page       = 10

admin.site.register(Fotografia, ListandoFotografias)