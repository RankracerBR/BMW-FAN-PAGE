from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Carro

# Create your views here.

def index(request):
    return render(request,'index.html')

def catalogo(request):
    return render(request,'catalogo.html')

def solicitar_financiamento(request):
    if request.method == 'POST':
        car_model = request.POST['car_model']
        loan_amount = request.POST['loan_amount']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        #calcular jurso aqui
        
        interest_rate = 0.05 
        
        Carro.objects.create(
            car_model = car_model,
            loan_amount = loan_amount,
            start_date = start_date,
            end_date = end_date,
            interest_rate = interest_rate
        )
        
    return render(request,'financiamento.html')