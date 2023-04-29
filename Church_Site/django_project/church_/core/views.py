from django.shortcuts import render
from django.core.mail import send_mail, send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        if  not name or not email or not message:
            mensagem = 'Todos os campos devem ser preenchidos'
        recipient_email = 'seuemail@example.com'
        
        send_mail(
            'Mensagem de ' + name,
            'Nome: {}\nEmail: {}\nMensagem: {}'.format(name, email, message),
            email,
            [recipient_email],
            fail_silently=False,
        )

        # Adiciona a variável de contexto 'success' com valor True
        context = {'success': True}

    else:
        context = {}

    return render(request, 'contact.html', context )

