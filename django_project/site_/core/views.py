from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Carro, Usuario, Car_User

# Create your views here.

def index(request):
    return render(request,'index.html')

def catalogo(request):
    return render(request,'catalogo.html')

def solicitar_financiamento(request):
    mensagem = None # Inicializa a mensagem como vazia
    if request.method == 'POST':
        user_2 = request.POST['user_2']
        car_model_2 = request.POST['car_model_2']
        loan_amount_2 = request.POST['loan_amount_2']
        start_date_2 = request.POST['start_date_2']
        end_date_2 = request.POST['end_date_2']
        
        if  not user_2 or not car_model_2 or not loan_amount_2 or not start_date_2 or not end_date_2:
            mensagem = 'Todos os campos devem ser preenchidos'
        else:
            #calcular juros aqui
            interest_rate_2 = 0.05 
            # Cálculo dos juros omitido
            
            # Criação do objeto Carro
            
            #Carro.objects.create(
            #    car_model = car_model,
            #    loan_amount = loan_amount,
            #    start_date = start_date,
            #    end_date = end_date,
            #    interest_rate_2 = interest_rate_2
            #)
            #Usuario.objects.create(
            #    nome = nome,
            #    sobrenome = sobrenome
            #)

            Car_User.objects.create(
                user_2 = user_2,
                car_model_2 = car_model_2,
                loan_amount_2 = loan_amount_2,
                start_date_2 = start_date_2,
                end_date_2 = end_date_2,
                interest_rate_2 = interest_rate_2
                )
            
            # Define a mensagem de sucesso
            mensagem = f'O FINANCIAMENTO FOI SOLICITADO COM SUCESSO! SENHOR(A): {user_2}'
    
    return render(request, 'financiamento.html', {'mensagem': mensagem})

