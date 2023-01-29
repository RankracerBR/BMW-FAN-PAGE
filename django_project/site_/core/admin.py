from django.contrib import admin
from core.models import Usuario, Veiculo, Financiamento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
     list_display = ('nome','sobrenome')
     list_filter = ('nome','sobrenome')
     
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco')


class FinanciamentoAdmin():
     pass

admin.site.register(Usuario, EventoAdmin) 
admin.site.register(Veiculo,VeiculoAdmin)