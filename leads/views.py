from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    status = request.GET.get('status')
    return render(request,'principal.html')

def valida(request):
    nome =request.POST.get('nome')
    email =request.POST.get('email')


    if len(nome) < 3 or len(email) < 10:
        return HttpResponse('Email ou senha invalidos')

    try:
        return render(request, 'envio.html',{'nome':nome,
                                            'email':email})
    except:
        return HttpResponse('erro interno do sistema')
