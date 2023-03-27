from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Carro, Usuario

# Create your views here.

def index(request):
    return render(request,'index.html')

def catalogo(request):
    return render(request,'catalogo.html')

def solicitar_financiamento(request):
    mensagem = None # Inicializa a mensagem como vazia
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        car_model = request.POST['car_model']
        loan_amount = request.POST['loan_amount']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        if not car_model or not loan_amount or not start_date or not end_date:
            mensagem = 'Todos os campos devem ser preenchidos'
        else:
            #calcular juros aqui
            interest_rate = 0.05 
            # Cálculo dos juros omitido
            
            # Criação do objeto Carro
            
            Carro.objects.create(
                car_model = car_model,
                loan_amount = loan_amount,
                start_date = start_date,
                end_date = end_date,
                interest_rate = interest_rate
            )
            Usuario.objects.create(
                nome = nome,
                sobrenome = sobrenome
            )

            # Define a mensagem de sucesso
            mensagem = f'O FINANCIAMENTO FOI SOLICITADO COM SUCESSO! SENHOR(A): {nome} {sobrenome}'
    
    return render(request, 'financiamento.html', {'mensagem': mensagem})

