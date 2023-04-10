from django.contrib import admin
from core.models import Usuario, Carro, Car_User
# Register your models here.

#Unused for a moment
class EventoAdmin(admin.ModelAdmin):
     list_display = ('nome','sobrenome')
     list_filter = ('nome','sobrenome')

#Unused for a moment   
class UsuarioAdmin(admin.ModelAdmin):
     list_display = ('nome','sobrenome')

#Unused for a moment
class CarroAdmin(admin.ModelAdmin):
     list_display=('car_model', 'loan_amount', 'start_date', 'end_date', 'interest_rate')

class Car_userAdmin(admin.ModelAdmin):
     list_display = ('user_2','car_model_2', 'loan_amount_2', 'start_date_2', 'end_date_2', 'interest_rate_2')

admin.site.register(Car_User,Car_userAdmin)

#Unused for a moment
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Carro, CarroAdmin)
