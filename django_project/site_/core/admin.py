from django.contrib import admin
from core.models import Usuario, Carro
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
     list_display = ('nome','sobrenome')
     list_filter = ('nome','sobrenome')
     
class CarroAdmin(admin.ModelAdmin):
     list_display=('car_model', 'loan_amount', 'start_date', 'end_date', 'interest_rate')
     

admin.site.register(Carro, CarroAdmin)
