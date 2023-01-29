from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Veiculo, Financiamento


# Create your views here.

def index(request):
    return render(request,'index.html')

def catalogo(request):
    return render(request,'catalogo.html')

def solicitar_financiamento(request):
    if request.method == 'POST':
        # Recupera os dados do formulário
        veiculo_id = request.POST.get('veiculo')
        valor_financiamento = request.POST.get('valor')
        juros = request.POST.get('juros')
        data_inicio = request.POST.get('data_inicio')
        data_vencimento = request.POST.get('data_vencimento')

        # Recupera o veículo selecionado
        veiculo = Veiculo.objects.get(pk=veiculo_id)

        # Calcula o valor final do financiamento com juros
        valor_final = valor_financiamento * (1 + juros / 100)

        # Salva o financiamento no banco de dados
        financiamento = Financiamento(veiculo=veiculo, juros=juros, valor=valor_final, data_inicio=data_inicio, data_vencimento=data_vencimento)
        financiamento.save()

        # Redireciona para a página de detalhes do financiamento
        return redirect('financiamento_detalhes', financiamento_id=financiamento.id)
    else:
        # Exibe a página com o formulário de solicitação de financiamento
        veiculos = Veiculo.objects.all()
        return render(request, 'financiamento.html', {'veiculos': veiculos})
